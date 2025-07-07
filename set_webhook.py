import telebot

TOKEN = "7419649484:AAGVTtcjwUVOotnOQU8zm71IGhxTctW1Tj8"
WEBHOOK_URL = "https://Telegram-bot.onrender.com/" + TOKEN

bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)
print("Webhook o'rnatildi:", WEBHOOK_URL)
