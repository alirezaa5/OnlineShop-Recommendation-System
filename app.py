import os
import pyodbc
from flask import Flask, render_template, abort

app = Flask(__name__)

SERVER = os.getenv("DB_SERVER", "localhost")
DATABASE = os.getenv("DB_NAME", "OnlineShop")
DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")


def get_connection():
    connection_string = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        "Trusted_Connection=yes;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(connection_string)


@app.route("/")
def home():
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT CategoryID, CategoryName
            FROM Categories
            ORDER BY CategoryName
        """)
        categories = cursor.fetchall()

        cursor.execute("""
            SELECT ProductID, ProductName, Description,
                   Price, StockQuantity, CategoryID
            FROM Products
            ORDER BY ProductName
        """)
        products = cursor.fetchall()

    return render_template("index.html", categories=categories, products=products)


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT ProductID, ProductName, Description,
                   Price, StockQuantity, CategoryID
            FROM Products
            WHERE ProductID = ?
        """, product_id)
        product = cursor.fetchone()

        if product is None:
            abort(404)

        # پیشنهاد محصولات دیگر از دسته‌بندی مشابه
        cursor.execute("""
            SELECT TOP 4 ProductID, ProductName, Description,
                         Price, StockQuantity, CategoryID
            FROM Products
            WHERE CategoryID = ?
              AND ProductID <> ?
              AND StockQuantity > 0
            ORDER BY StockQuantity DESC, Price ASC
        """, product.CategoryID, product.ProductID)
        recommendations = cursor.fetchall()

    return render_template(
        "product.html",
        product=product,
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)
