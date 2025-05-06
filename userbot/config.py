import os

DEVS = [
    1927018403
]

API_ID = int(os.getenv("API_ID", "27418440"))

API_HASH = os.getenv("API_HASH", "0a08a360e0e9f41b9896f655c300d09d")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8123679703:AAHnB7LpUtfEKvYQdJslVzb5kq61IlKMHII")

OWNER_ID = int(os.getenv("OWNER_ID", "1927018403"))

USER_ID = list(map(int,os.getenv("USER_ID", "1927018403",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002547370737"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002547370737").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Kinaya:KontolXD#123@kinaya.yuf2elr.mongodb.net/?retryWrites=true&w=majority&appName=Kinaya")
