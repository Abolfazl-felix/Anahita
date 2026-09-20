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
    text = """🎉🎂 تولدت مبارک خوشگل خانم 💖

امیدوارم امسال یه سال پر از سلامتی، شادی، آرامش و کلی لبخندهای قشنگ برات باشه 🌸✨
امیدوارم به همه آرزوهای قشنگت برسی و هر روزت از روز قبل بهتر و روشن‌تر باشه 🤍🌷

دوست دارم همیشه گیت پر از لبخند باشه و هیچ‌وقت غم مهمون دلت نشه 🌹🫶

با آرزوی بهترین‌ها برات
از طرف دوست همیشگیت و کادو دهنده دفتر رنگ‌آمیزی 🎨📖💝

تولدت هزاران بار مبارک 🎁🎈🎂"""
else:
    text = "🎂 تولد آناهیتا گذشته ❤️"

async def main():
    bot = Bot(TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=text)

asyncio.run(main())