from telegram import Bot
from persiantools.jdatetime import JalaliDate
from datetime import date
import asyncio
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = -1004297391995

# تولد: ۳۰ آذر ۱۴۰۵
birthday = JalaliDate(1405, 9, 30).to_gregorian()
today = date.today()

days = (birthday - today).days

if days > 0:
    text = f"🎂❤️ تا تولد آناهیتا {days} روز مونده 🎉"
elif days == 0:
    text = "🎉🎂 امروز تولد آناهیتاست ❤️"
else:
    text = "🎂 تولد آناهیتا گذشته ❤️"
async def main():
    bot = Bot(TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=text)

asyncio.run(main())