import telebot
import yt_dlp
import os

TOKEN = "7633395197:AAFwAsT0Xn9ut76JA99LnmD_IGbrJwKvcrY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text
    
    if "http" not in url:
        bot.reply_to(message, "Линк фиристӣ? Ман танҳо линкро мефаҳмам.")
        return

    bot.reply_to(message, "📹 Видео бор мешавад... 1 дақиқа интизор шав.")

    try:
        ydl_opts = {
            'outtmpl': 'video.%(ext)s',
            'format': 'best[filesize<1800M]',
            'noplaylist': True,
            'quiet': True,
            'cookiesfrombrowser': ('chrome',)
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        with open(filename, 'rb') as video:
            bot.send_document(message.chat.id, video, caption="✅ Тайёр!")

        os.remove(filename)

    except Exception as e:
        bot.reply_to(message, f"Хато: {e}")

print("Бот кор мекунад...")
bot.polling(none_stop=True)