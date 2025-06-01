import os

DEVS = [
    6904648429
]

API_ID = int(os.getenv("API_ID", "26550183"))

API_HASH = os.getenv("API_HASH", "25be30608ef422623c7d8a55bfb98c62")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7909712343:AAGjKLcNyWTyoGTWK_nmdbzaA4ZMkajG1b0")

OWNER_ID = int(os.getenv("OWNER_ID", "6904648429"))

USER_ID = list(map(int,os.getenv("USER_ID", "6904648429",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002557925562"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002620633078").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://bapakloanjing:KontolXD#123@bapakloanjing.muyhagw.mongodb.net/?retryWrites=true&w=majority&appName=bapakloanjing")
