from telegram import Bot
from persiantools.jdatetime import JalaliDate
from datetime import date
import asyncio
import os
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = -1004297391995
bot = Bot(token=TOKEN)
today = JalaliDate.today()
birthday = JalaliDate(1405, 9, 30)
days = (birthday.to_gregorian() - date.today()).days
if days > 0:
    text = f"🎂❤️ تا تولد آناهیتا {days} روز مونده 🎉"
elif days == 0:
    text = "🎉🎂 امروز تولد آناهیتاست ❤️"
else
    text = "🎉 تولد آناهیتا گذشته ❤️"
async def send():
    await bot.send_message(chat_id=CHAT_ID, text=text)
asyncio.run(send())
