
import os
import yt_dlp
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling 

TOKEN = ""
7633395197:AAHeSWP4wCkJHlVfvr5_Z3ec_2zV0aIOcr8
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Салом! Линки YouTube, Instagram ё TikTok-ро фирист, видеояшро мегирам.")

@dp.message_handler()
async def download(message: types.Message):
    url = message.text
    if "youtube.com" not in url and "youtu.be" not in url and "instagram.com" not in url and "tiktok.com" not in url:
        await message.reply("Лутфан танҳо линки YouTube, Instagram ё TikTok фирист.")
        return
    
    await message.reply("Видеоро мегирам, 1 дақиқа интизор шав...")
    
    try:
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': 'video.mp4',
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        await bot.send_video(message.chat.id, video=open('video.mp4', 'rb'))
        os.remove('video.mp4')
        
    except Exception as e:
        await message.reply(f"Хато шуд: {e}")

if name == 'main':
    start_polling(dp, skip_updates=True)
