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
if days > 100:
    text = f"🎂 تا تولد آناهیتا {days} روز باقی مانده ❤️"

elif days == 100:
    text = "💯 فقط 100 روز تا تولد آناهیتا مونده 🎉"

elif days > 50:
    text = f"🎂 تا تولد آناهیتا {days} روز باقی مانده ❤️"

elif days == 50:
    text = "🌸 فقط 50 روز مونده تا روز قشنگت 💖"

elif days > 30:
    text = f"🎂 تا تولد آناهیتا {days} روز باقی مانده ❤️"

elif days == 30:
    text = """✨ فقط 30 روز مونده

کم‌کم داریم به روز قشنگت نزدیک می‌شیم 🌷"""

elif days > 14:
    text = f"🎂 تا تولد آناهیتا {days} روز باقی مانده ❤️"

elif days == 14:
    text = "💖 فقط دو هفته تا تولدت مونده ✨"

elif days > 7:
    text = f"🎂 تا تولد آناهیتا {days} روز باقی مانده ❤️"

elif days == 7:
    text = "🎈 فقط یک هفته تا تولدت مونده ❤️"

elif days > 3:
    text = f"🎂 تا تولد آناهیتا {days} روز باقی مانده ❤️"

elif days == 3:
    text = "🎁 فقط 3 روز دیگه تا تولدت مونده 🥳"

elif days == 2:
    text = "💕 فقط 2 روز مونده... 🤍"

elif days == 1:
    text = """🌙 فردا تولدته...

امیدوارم فردا یکی از قشنگ‌ترین روزهای زندگیت باشه 🤍✨"""

elif days == 0:
    text = """🎉🎂 تولدت مبارک خوشگل خانم 💖

امیدوارم امسال یه سال پر از سلامتی، شادی، آرامش و کلی لبخندهای قشنگ برات باشه 🌸✨
امیدوارم به همه آرزوهای قشنگت برسی و هر روزت از روز قبل بهتر و روشن‌تر باشه 🤍🌷

دوست دارم همیشه گیت پر از لبخند باشه و هیچ‌وقت غم مهمون دلت نشه 🌹🫶

با آرزوی بهترین‌ها برات
از طرف دوست همیشگیت و کادو دهنده دفتر رنگ‌آمیزی 🎨📖💝

تولدت هزاران بار مبارک 🎁🎈🎂"""

else:
    text = "🎂 تولد امسال گذشت، حالا منتظر سال بعد می‌مونیم ❤️"

async def main():
    bot = Bot(TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=text)

asyncio.run(main())