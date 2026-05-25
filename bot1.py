import os
import telebot
from yt_dlp import YoutubeDL

TOKEN = "7633395197:AAHeSWP4wCkJHlVfvr5_Z3ec_2zV0aIOcr8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! Linki YouTube firist")

@bot.message_handler(func=lambda m: True)
def download(message):
    url = message.text.strip()
    
    if "youtube.com" not in url and "youtu.be" not in url:
        bot.send_message(message.chat.id, "Faqat linki YouTube firist")
        return
    
    bot.send_message(message.chat.id, "Video bor meshavad...")
    
    try:
        ydl_opts = {
            'outtmpl': 'video.mp4',
            'format': 'best[height<=720]',
            'quiet': True
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        with open('video.mp4', 'rb') as video:
            bot.send_video(message.chat.id, video)
        
        os.remove('video.mp4')
        
    except:
        bot.send_message(message.chat.id, "Khata: Video girifta nashud")

if __name__ == "__main_":
    bot.polling(none_stop=True)
