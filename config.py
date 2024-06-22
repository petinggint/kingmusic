from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7200"))

OWNER_ID = int(getenv("OWNER_ID", "7463772447"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/edd188500491cf42164e7.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/edd188500491cf42164e7.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kingmusicsupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Asupanredglorysex")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7463772447").split()))


FAILED = "https://graph.org/file/edd188500491cf42164e7.jpg"
