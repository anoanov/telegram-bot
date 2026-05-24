import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from yt_dlp import YoutubeDL

TOKEN = "7633395197:AAFwAsT0Xn9ut76JA99LnmD_IGbrJwKvcrY"
bot = telebot.TeleBot(TOKEN)

TEXTS = {
    "tg": {
        "start": "Салом! 🌸 Забонро интихоб кунед:",
        "ask_link": "Линки YouTube, Instagram, TikTok фирист 🌸",
        "downloading": "Видео бор мешавад, 1 дақиқа интизор шав 🌸",
        "error": "Хатогӣ рух дод: {}",
        "wrong_link": "Фақат линки YouTube, Instagram, TikTok фирист 🌸"
    },
    "ru": {
        "start": "Привет! 🌸 Выберите язык:",
        "ask_link": "Отправьте ссылку YouTube, Instagram, TikTok 🌸",
        "downloading": "Видео загружается, подождите 1 минуту 🌸",
        "error": "Произошла ошибка: {}",
        "wrong_link": "Отправляйте только ссылки YouTube, Instagram, TikTok 🌸"
    },
    "en": {
        "start": "Hello! 🌸 Choose a language:",
        "ask_link": "Send me a YouTube, Instagram, TikTok link 🌸",
        "downloading": "Video is downloading, please wait 1 minute 🌸",
        "error": "Error occurred: {}",
        "wrong_link": "Please send only YouTube, Instagram, TikTok links 🌸"
    }
}

user_lang = {}

def get_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("Тоҷикӣ", callback_data="lang_tg"),
        InlineKeyboardButton("Русский", callback_data="lang_ru"),
        InlineKeyboardButton("English", callback_data="lang_en")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, TEXTS["tg"]["start"], reply_markup=get_keyboard())

@bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
def set_language(call):
    lang = call.data.split("_")[1]
    user_lang[call.from_user.id] = lang
    bot.edit_message_text(TEXTS[lang]["ask_link"], call.message.chat.id, call.message_id)

@bot.message_handler(func=lambda m: True)
def download_video(message):
    lang = user_lang.get(message.from_user.id, "tg")
    url = message.text

    if not any(x in url for x in ["youtube.com", "youtu.be", "instagram.com", "tiktok.com"]):
        bot.send_message(message.chat.id, TEXTS[lang]["wrong_link"])
        return

    bot.send_message(message.chat.id, TEXTS[lang]["downloading"])

    ydl_opts = {
        'outtmpl': 'video.%(ext)s',
        'format': 'best[height<=720][filesize<50M]',
        'noplaylist': True,
        'quiet': True,
        'nocheckcertificate': True,
        'merge_output_format': 'mp4'
    }

    if os.path.exists('cookies.txt'):
        ydl_opts['cookiefile'] = 'cookies.txt'

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        file_size = os.path.getsize(filename) / (1024 * 1024)
        if file_size > 50:
            bot.send_message(message.chat.id, "Видео калон аст. Макс 50MB мешавад 🌸")
            os.remove(filename)
            return

        with open(filename, 'rb') as video:
            bot.send_video(message.chat.id, video)

        os.remove(filename)

    except Exception as e:
        bot.send_message(message.chat.id, TEXTS[lang]["error"].format(str(e)[:200]))

bot.polling(none_stop=True)
