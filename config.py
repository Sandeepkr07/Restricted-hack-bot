# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24558120"))
API_HASH = getenv("API_HASH", "85bd1a317c44733e6620ec82a7053fe9")
BOT_TOKEN = getenv("BOT_TOKEN", "7264260495:AAG_nyJj_vAkQ_bS_8ogVxib8py9iz7gLuY")
OWNER_ID = int(getenv("OWNER_ID", "6005294654"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://sandeepkrbth64:NbPbc81D9Z7CXhLj@sandeepkr.5zk8q.mongodb.net/?retryWrites=true&w=majority&appName=Sandeepkr")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002381172477"))
FORCESUB = getenv("FORCESUB", "-1002325159591")
