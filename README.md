# پروژه فروشگاه آنلاین (OnlineShop)

نمونه ساده فروشگاه اینترنتی با Python، Flask و SQL Server.

## امکانات
- خواندن دسته‌بندی‌ها و محصولات از SQL Server
- نمایش فهرست و جزئیات محصولات
- پیشنهاد حداکثر چهار محصول دیگر از دسته‌بندی مشابه

## جدول‌های مورد استفاده
- `Categories(CategoryID, CategoryName)`
- `Products(ProductID, ProductName, Description, Price, StockQuantity, CategoryID)`

## تنظیم اتصال
مقادیر پیش‌فرض: سرور `localhost`، پایگاه داده `OnlineShop` و Windows Authentication.
در صورت نیاز متغیرهای محیطی `DB_SERVER`، `DB_NAME` و `DB_DRIVER` قابل تغییرند.
درایور پیش‌فرض: `ODBC Driver 18 for SQL Server`.

## نصب وابستگی‌ها
```bash
pip install -r requirements.txt
```

## اجرا
```bash
python app.py
```
سپس `http://127.0.0.1:5000` را باز کنید.

## روش پیشنهاددهی
با باز شدن صفحه یک محصول، برنامه شناسه دسته‌بندی آن را می‌گیرد و حداکثر چهار محصول دیگر از همان دسته را پیشنهاد می‌دهد. محصول فعلی و محصولات بدون موجودی حذف می‌شوند. اولویت نمایش با موجودی بیشتر و سپس قیمت کمتر است. این روش یک پیشنهاددهنده ساده مبتنی بر محتوا (Content-Based) است و از یادگیری ماشین استفاده نمی‌کند.
