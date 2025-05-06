import os

DEVS = [
    5646661182
]

API_ID = int(os.getenv("API_ID", "22146045"))

API_HASH = os.getenv("API_HASH", "80807ed4e66a8d60d30645a390a35163")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7609025339:AAEvlo_3Zj8XuZtWgKPfzs6awMTZsD8Wvrg")

OWNER_ID = int(os.getenv("OWNER_ID", "5646661182"))

USER_ID = list(map(int,os.getenv("USER_ID", "5646661182",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002486020552"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002486020552").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://yunadallenbot:asmaralokamujomok12321@cluster0.j3dr1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
