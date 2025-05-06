# database.py

# Misalkan menggunakan dictionary untuk menyimpan data sementara
database = {}

async def set_vars(user_id, key, value):
    if user_id not in database:
        database[user_id] = {}
    database[user_id][key] = value

async def get_vars(user_id, key):
    return database.get(user_id, {}).get(key)

async def remove_vars(user_id, key):
    if user_id in database and key in database[user_id]:
        del database[user_id][key]

