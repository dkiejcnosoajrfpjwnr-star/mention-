# 🚀 تشغيل Mention-All-Bot

## خطوات سريعة للتشغيل

### 1️⃣ احصل على Bot Token

```
1. افتح Telegram وابحث عن: @BotFather
2. أرسل: /newbot
3. اتبع التعليمات
4. انسخ Token
```

---

### 2️⃣ حضر الملفات

```bash
# استنسخ المشروع
git clone https://github.com/dkiejcnosoajrfpjwnr-star/mention-.git
cd mention-

# أنشئ ملف .env
cp .env.example .env

# اضفع Token في .env
nano .env
# ثم غير: TGBOT_TOKEN=YOUR_BOT_TOKEN_HERE
```

---

### 3️⃣ شغل البوت

#### **الطريقة 1: Docker Compose (الأسهل)**

```bash
docker-compose up -d
```

✅ البوت يشتغل الآن!

#### **الطريقة 2: Docker البسيط**

```bash
docker run -d \
  --name mention-bot \
  -e TGBOT_TOKEN="YOUR_BOT_TOKEN_HERE" \
  --restart always \
  -v $(pwd)/database.db:/app/database.db \
  -v $(pwd)/logs:/app/logs \
  ghcr.io/dkiejcnosoajrfpjwnr-star/mention-all-bot:master
```

#### **الطريقة 3: محلي (للتطوير)**

```bash
# ثبت المتطلبات
pip install -r requirements.txt

# شغل البوت
export TGBOT_TOKEN="YOUR_BOT_TOKEN_HERE"
python app.py
```

---

### 4️⃣ اختبر البوت

افتح Telegram وابحث عن بوتك، ثم:

```
/start          - بدء البوت
/in             - الدخول (للحصول على mentions)
/all            - ذكر الجميع المسجلين
/out            - الخروج
/stats          - إحصائيات البوت
```

---

### 5️⃣ التحكم في البوت

#### مشاهدة السجلات:
```bash
docker logs -f mention-all-bot
```

#### إيقاف البوت:
```bash
docker-compose down
# أو
docker stop mention-all-bot
```

#### إعادة تشغيل:
```bash
docker-compose restart
# أو
docker restart mention-all-bot
```

#### حذف البوت:
```bash
docker-compose down -v
# أو
docker rm -f mention-all-bot
```

---

## 🔧 استكشاف الأخطاء

### المشكلة: "Token غير صحيح"
✅ تأكد من نسخ Token بشكل صحيح من @BotFather

### المشكلة: "البوت لا يرد"
✅ تحقق من السجلات: `docker logs mention-all-bot`
✅ تأكد من أن اتصالك بالإنترنت يعمل

### المشكلة: "خطأ في Database"
✅ احذف database.db وأعد التشغيل:
```bash
rm database.db
docker-compose restart
```

---

## 📊 معلومات مفيدة

- 🐳 Docker Image: `ghcr.io/dkiejcnosoajrfpjwnr-star/mention-all-bot:master`
- 📁 Database: `database.db` (SQLite)
- 📝 Logs: `logs/` أو `logs.log`
- 🔗 Repository: https://github.com/dkiejcnosoajrfpjwnr-star/mention-

---

**استمتع بـ Mention-All-Bot! 🎉**
