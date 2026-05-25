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
        "downloading": "⏳ Видео бор мешавад, 1 дақиқа интизор шав",
        "done": "✅ Тайёр!",
        "error": "❌ Хатогӣ: {}",
        "wrong_link": "❌ Фақат линки YouTube, Instagram, TikTok фирист",
        "big_file": "❌ Видео калон аст. Макс 50MB мешавад"
    },
    "ru": {
        "start": "Привет! 🌸 Выберите язык:",
        "ask_link": "Отправьте ссылку YouTube, Instagram, TikTok 🌸",
        "downloading": "⏳ Видео загружается, подождите 1 минуту",
        "done": "✅ Готово!",
        "error": "❌ Ошибка: {}",
        "wrong_link": "❌ Отправляйте только ссылки YouTube, Instagram, TikTok",
        "big_file": "❌ Видео слишком большое. Макс 50MB"
    },
    "en": {
        "start": "Hello! 🌸 Choose a language:",
        "ask_link": "Send me a YouTube, Instagram, TikTok link 🌸",
        "downloading": "⏳ Video is downloading, please wait 1 minute",
        "done": "✅ Done!",
        "error": "❌ Error: {}",
        "wrong_link": "❌ Please send only YouTube, Instagram, TikTok links",
        "big_file": "❌ Video is too large. Max 50MB"
    }
}

user_lang = {}

def get_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("🇹🇯 Тоҷикӣ", callback_data="lang_tg"),
        InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
        InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
    )
    return markup
