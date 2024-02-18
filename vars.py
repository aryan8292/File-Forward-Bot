from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "forward bot")
API_ID = "3334521"
API_HASH = "29edd7420d528140c7a04bd47486886f"
BOT_TOKEN = environ["BOT_TOKEN"]
LOG_CHANNEL = "-1002063406137"
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5079629749').split()]
TARGET_DB = int(environ.get("TARGET_DB", "-1002131448296"))
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/Joelkb/File-Forward-Bot")
