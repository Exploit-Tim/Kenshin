import os

DEVS = [
    1927018403
]

API_ID = int(os.getenv("API_ID", "28472248"))

API_HASH = os.getenv("API_HASH", "103f9d22b7b00c73c03861930fd9cf3c")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8168163692:AAF8mi2Jnd9lgALdmyaHRrDSCaqb82oUh30")

OWNER_ID = int(os.getenv("OWNER_ID", "1927018403"))

USER_ID = list(map(int,os.getenv("USER_ID", "1927018403",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002197595899"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002620633078").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Kinaya:KontolXD#123@kinaya.yuf2elr.mongodb.net/?retryWrites=true&w=majority&appName=Kinaya")
