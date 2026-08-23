# Mention-All-Bot 🚀

بوت تيليجرام ذكي يساعدك على ذكر جميع أعضاء المجموعة بسهولة!

**A smart Telegram bot that helps you mention all group members easily!**

---

## ✨ المميزات | Features

✅ ذكر جميع الأعضاء المسجلين بأمر واحد  
✅ تسجيل الدخول والخروج بسهولة  
✅ إحصائيات المستخدمين والمجموعات  
✅ دعم مجموعات متعددة  
✅ محفوظ الرسائل والبيانات  

---

## 🚀 البدء السريع | Quick Start

### الطريقة 1: Docker Compose (الأسهل)
```bash
# استنسخ المشروع
git clone https://github.com/dkiejcnosoajrfpjwnr-star/mention-.git
cd mention-

# أنشئ ملف البيئة
cp .env.example .env

# عدّل Token (افتح .env وضع Token من @BotFather)
nano .env

# شغل البوت
docker-compose up -d
```

### الطريقة 2: Docker البسيط
```bash
docker run -d \
  --name mention-bot \
  -e TGBOT_TOKEN="YOUR_TOKEN_HERE" \
  --restart always \
  -v $(pwd)/database.db:/app/database.db \
  -v $(pwd)/logs:/app/logs \
  ghcr.io/dkiejcnosoajrfpjwnr-star/mention-all-bot:master
```

### الطريقة 3: محلي (للتطوير)
```bash
# ثبت المتطلبات
pip install -r requirements.txt

# شغل البوت
export TGBOT_TOKEN="YOUR_TOKEN_HERE"
python app.py
```

---

## 📝 أوامر البوت | Bot Commands

| الأمر | الوصف |
|------|--------|
| `/start` | عرض رسالة الترحيب |
| `/in` | تسجيل الدخول (للحصول على mentions) |
| `/all` | ذكر جميع الأعضاء المسجلين |
| `/out` | الخروج من النظام |
| `/stats` | عرض الإحصائيات |

---

## 🛠️ المتطلبات | Requirements

- Docker & Docker Compose
- Python 3.12+ (للتشغيل المحلي)
- Telegram Bot Token من @BotFather

---

## 📊 البيانات والسجلات | Data & Logs

- 📁 `database.db` - قاعدة البيانات (SQLite)
- 📝 `logs/` - سجلات التشغيل

---

## 🐛 استكشاف الأخطاء | Troubleshooting

### البوت لا يستجيب
```bash
# افحص السجلات
docker logs -f mention-all-bot

# تأكد من صحة Token
# تحقق من الاتصال بالإنترنت
```

### مشكلة في البيانات
```bash
# احذف قاعدة البيانات والبدء من جديد
rm database.db
docker-compose restart
```

---

## 📜 الترخيص | License

GNU General Public License v3.0

---

## 👨‍💻 التطوير | Development

```bash
# نسخ المتطلبات
pip install -r requirements.txt

# تشغيل البوت محلياً
python app.py

# مراقبة السجلات
tail -f logs.log
```

---

**استمتع بـ Mention-All-Bot! 🎉**
