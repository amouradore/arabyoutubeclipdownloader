# تحميل مقاطع يوتيوب

هذا المشروع عبارة عن تطبيق Python مع واجهة رسومية (Tkinter) باللغة العربية يتيح لك تحميل مقطع (محدد بفاصل زمني) من فيديو YouTube باستخدام pytube.

## المميزات

- تحميل مقطع فيديو: حدد رابط الفيديو، وقت البداية ووقت النهاية (بالدقائق) لاستخراج الجزء المطلوب.
- واجهة رسومية باللغة العربية: استخدام Tkinter لتجربة سهلة وبديهية.
- اختيار مجلد الحفظ: زر "تصفح" يسمح بتحديد موقع حفظ الملف.

## المتطلبات الأساسية

- Python 3 أو أحدث
- pytube (يتم تثبيته عبر ملف requirements.txt)
- Tkinter (مضمن مع Python في معظم التوزيعات)

## التثبيت

نسخ المستودع:

git clone https://github.com/votre-utilisateur/arabyoutubeclipdownloader.git
cd arabic-youtube-downloader

(اختياري) إنشاء وتفعيل البيئة الافتراضية:

python -m venv venv
source venv/bin/activate  # لنظام Windows : venv\Scripts\activate

تثبيت المتطلبات:

pip install -r requirements.txt

## طريقة الاستخدام

قم بتشغيل البرنامج الرئيسي:

python arabyoutubeclipdownloader.py

في النافذة التي تظهر:
1. قم بلصق رابط فيديو YouTube
2. أدخل وقت البداية بالدقائق
3. أدخل وقت النهاية بالدقائق
4. اختر مكان الحفظ باستخدام زر "تصفح"
5. انقر على "تحميل" لبدء التحميل

## الكود المصدري
