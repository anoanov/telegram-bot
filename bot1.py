import telebot
import yt_dlp
import os

TOKEN = "7633395197:AAFwAsT0Xn9ut76JA99LnmD_IGbrJwKvcrY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Салом! Линки TikTok, YouTube, Instagram-ро фирист, ман видеоашро мефиристам ✅")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text
    
    if "http" not in url:
        bot.reply_to(message, "Линк фиристӣ? Ман танҳо линкро мефаҳмам.")
        return
    
    bot.reply_to(message, "⏳ Видео бор мешавад, 1 дақиқа интизор шав...")
    
    try:
        ydl_opts = {
            'outtmpl': 'video.%(ext)s',
            'format': 'mp4',
            'max_filesize': 50*1024*1024,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        
        with open(filename, 'rb') as video:
            bot.send_video(message.chat.id, video)
        
        os.remove(filename)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Хато: Видео бор نشуд. Сабаб: {str(e)}")

bot.polling(none_stop=True)