import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Database 
DB_URI = os.environ.get("DB_URI", "")

#Your Logs Channel/Group ID
LOGS_CHAT_ID = int(os.environ.get("LOGS_CHAT_ID", ""))

#Force Sub Channel Invite Link
FSUB_INV_LINK = os.environ.get("FSUB_INV_LINK", "")
