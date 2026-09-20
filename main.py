from telegram import Bot
from datetime import date
import random
import asyncio
import os

from birthdays import PEOPLE
from messages import MESSAGES

TOKEN = os.environ["BOT_TOKEN"]


def build_text(person):
    birthday = person["birthday"]
    today = date.today()

    days = (birthday - today).days

    name = person["name"]
    symbol = person["theme"]["symbol"]
    flower = person["theme"]["flower"]

    header = f"""━━━━━━━━━━━━
{symbol} {name} {flower}
━━━━━━━━━━━━

"""

    normal_messages = MESSAGES[person["message_type"]]

        if days > 100:
        text = random.choice(normal_messages).format(days=days)

    elif days == 100:
        text = f"💯 فقط 100 روز تا تولد {name} مونده 🎉"

    elif days > 50:
        text = random.choice(normal_messages).format(days=days)

    elif days == 50:
        text = f"🌸 فقط 50 روز تا تولد {name} مونده 💖"

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
        text = person["birthday_message"]

    else:
        text = f"🎂 تولد {name} امسال گذشت، حالا منتظر سال بعد می‌مونیم ❤️"

    return header + text
async def main():
    bot = Bot(TOKEN)

    for person in PEOPLE:
        text = build_text(person)

        for chat_id in person["chat_ids"]:
            await bot.send_message(
                chat_id=chat_id,
                text=text
            )


if __name__ == "__main__":
    asyncio.run(main())