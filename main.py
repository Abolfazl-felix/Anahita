from telegram import Bot
from persiantools.jdatetime import JalaliDate
from datetime import date
import random
import asyncio
import os

TOKEN = os.environ["BOT_TOKEN"]

PEOPLE = [
    {
        "name": "آناهیتا",
        "birthday": JalaliDate(1405, 9, 30).to_gregorian(),
        "chat_ids": [
            -1004297391995,
            -1004356259615
        ],
        "theme": {
            "emoji": "🌙💜🌺",
            "symbol": "🌙",
            "flower": "🌺",
            "style": "moon"
        },
        "messages": [
            "🌸 تا تولد آناهیتا {days} روز باقی مونده 💖",
            "✨ فقط {days} روز تا روز قشنگت مونده 🤍",
            "🎂 شمارش معکوس ادامه داره... {days} روز باقی مونده ❤️",
            "🌷 هر روز داریم به تولدت نزدیک‌تر می‌شیم... {days} روز مونده 🫶",
            "💝 فقط {days} روز دیگه تا لبخندهای روز تولدت 🎉",
            "🌙 امروز هم یه روز کمتر شد... {days} روز باقی مونده 🤍",
            "🎈 هنوز {days} روز مونده، ولی هیجانش از الان شروع شده 💕",
            "☀️ روزهای باقی‌مونده: {days} 🌸",
        ]
    },
{
    "name": "مائده",
    "birthday": JalaliDate(1405, 7, 23).to_gregorian(),
    "chat_ids": [
        -1004356259615
    ],
    "theme": {
        "emoji": "🐺🖤🌹",
        "symbol": "🐺",
        "flower": "🌹",
        "style": "wolf"
    },
    "messages": [
        "🌹 تا تولد مائده {days} روز باقی مونده 🐺",
        "✨ فقط {days} روز تا روز قشنگت مونده 🤍",
        "🎂 شمارش معکوس ادامه داره... {days} روز باقی مونده ❤️",
        "🌷 هر روز داریم به تولدت نزدیک‌تر می‌شیم... {days} روز مونده 🫶",
        "💝 فقط {days} روز دیگه تا روز تولدت 🎉",
        "🐺 امروز هم یه روز کمتر شد... {days} روز باقی مونده 🖤",
        "🎈 هنوز {days} روز مونده، ولی هیجانش از الان شروع شده 💕",
        "☀️ روزهای باقی‌مونده: {days} 🌹"
    ]
}
]
def build_text(person):
    birthday = person["birthday"]
    today = date.today()

    days = (birthday - today).days
    normal_messages = person["messages"]
    name = person["name"]
symbol = person["theme"]["symbol"]
flower = person["theme"]["flower"]

header = f"""━━━━━━━━━━━━
{symbol} {name} {flower}
━━━━━━━━━━━━

"""

    if days > 100:
        text = random.choice(normal_messages).format(days=days)

    elif days == 100:
        text = f"💯 فقط 100 روز تا تولد {name} مونده 🎉"

    elif days > 50:
        text = random.choice(normal_messages).format(days=days)

    elif days == 50:
        text = f"🌸 فقط 50 روز مونده تا روز قشنگ {name} 💖"

    elif days > 30:
        text = random.choice(normal_messages).format(days=days)

    elif days == 30:
        text = f"""✨ فقط 30 روز مونده

کم‌کم داریم به روز قشنگ {name} نزدیک می‌شیم 🌷"""

    elif days > 14:
        text = random.choice(normal_messages).format(days=days)

    elif days == 14:
        text = f"💖 فقط دو هفته تا تولد {name} مونده ✨"

    elif days > 7:
        text = random.choice(normal_messages).format(days=days)

    elif days == 7:
        text = f"🎈 فقط یک هفته تا تولد {name} مونده ❤️"

    elif days > 3:
        text = random.choice(normal_messages).format(days=days)

    elif days == 3:
        text = f"🎁 فقط 3 روز دیگه تا تولد {name} مونده 🥳"

    elif days == 2:
        text = f"💕 فقط 2 روز تا تولد {name} مونده 🤍"

    elif days == 1:
        text = f"""🌙 فردا تولد {name} است...

امیدوارم فردا یکی از قشنگ‌ترین روزهای زندگیت باشه 🤍✨"""

    elif days == 0:
        text = f"""🎉🎂 تولدت مبارک {name} 💖

امیدوارم امسال یه سال پر از سلامتی، شادی، آرامش و کلی لبخندهای قشنگ برات باشه 🌸✨
امیدوارم به همه آرزوهای قشنگت برسی و هر روزت از روز قبل بهتر و روشن‌تر باشه 🤍🌷

دوست دارم همیشه دلت پر از لبخند باشه و هیچ‌وقت غم مهمون دلت نشه 🌹🫶

با آرزوی بهترین‌ها برات
از طرف دوستدار همیشگیت و کادو دهنده دفتر رنگ‌آمیزی 🎨📖💝

تولدت هزاران بار مبارک 🎁🎈🎂"""

    else:
        text = f"🎂 تولد {name} امسال گذشت، حالا منتظر سال بعد می‌مونیم ❤️"

    return text


async def main():
    bot = Bot(TOKEN)

    for person in PEOPLE:
        text = build_text(person)

        for chat_id in person["chat_ids"]:
            await bot.send_message(
                chat_id=chat_id,
                text=text
            )

asyncio.run(main())