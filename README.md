# Telegram Instagram Login Bot

Bu Telegram bot Flask va webhook orqali ishlaydi. Bot foydalanuvchidan Instagram username va parolni so‘raydi va sizga yuboradi.

## 🔧 Fayllar

- `main.py` — Bot kodi (Flask + Telebot bilan)
- `requirements.txt` — kerakli Python kutubxonalar
- `Procfile` — Render.com uchun ishga tushirish fayli
- `set_webhook.py` — Webhook ulash uchun

## 🚀 Qanday ishlatish

### 1. GitHub’ga barcha fayllarni yuklang

Quyidagilar bo‘lishi kerak:
- `main.py`
- `requirements.txt`
- `Procfile`
- `set_webhook.py`

### 2. Render.com orqali deploy qilish

- `render.com` saytiga kiring
- "New Web Service" yarating
- GitHub repo’ni ulang
- Deploy qiling

### 3. Webhook sozlash

Render’da deploy bo‘lgach, terminalda quyidagini ishga tushiring:

```bash
python set_webhook.py
