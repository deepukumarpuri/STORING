# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
**THIS BOT SEND MOVIE FROM YOUTUBE WANT ANY MOVIES SUBSCRIBE MY YOUTUBE CHANNEL AND COMMENT ME YOUTUBE CHANNEL.**

SUBSCRIBE :- https://www.youtube.com/channel/UCosYJsNmv_n3VkMb01Ipq6w
🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @DKBOTZHELP

👥 **Support Group:** [DK BOTZ](https://t.me/DK_BOTZ)

📢 **Updates Channel:** [DK BOTZ](https://t.me/ROYAL_TECH_OFFICIAL)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @DKBOTZHELP

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @DKBOTZHELP

👥 **Support Group:** [DK BOTZ](https://t.me/DK_BOTZ)

📢 **Updates Channel:** [DK BOTZ](https://t.me/ROYAL_TECH_OFFICIAL)

"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot.**

**Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check About Bot Button**
"""
