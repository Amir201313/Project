[app]
title = Cornix Winner
package.name = cornixwinner
package.domain = org.bryandavids
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,json
version = 1.0.0

# پیش‌نیازهای کالیبره‌شده جهت پایداری بالا در زمان کامپایل کدهای فارسی
requirements = python3,kivy,pillow,arabic_reshaper,python-bidi==0.4.2,six

# فایل‌های آیکون و تصویر آغازین
icon.filename = icon.png
presplash.filename = Cornix.jpg

# جهت چرخش صفحه به صورت عمودی
orientation = portrait

# عدم پنهان‌سازی کلیدهای هوم و بک پایین گوشی
android.fullscreen = 0

# مجوزها و کدهای سیستمی اندروید ۵ و بالاتر
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.html = False
android.manifest.application_arguments = android:requestLegacyExternalStorage="true"

[buildozer]
log_level = 2
warn_on_root = 1
