from os import getenv

API_ID = int(getenv("API_ID", "26561490")) #optional
API_HASH = getenv("API_HASH", "1cf95f489c37be14568c94a8d09916b8") #optional

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_URL = getenv("MONGO_URL", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
LOG_GROUP = getenv("LOG_GROUP", "")
PM_LOGGER = getenv("PM_LOGGER", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5368154755").split()))
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/bhausetup/cherryubot")
BRANCH = getenv("BRANCH", "master") #don't change
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/7c1dffc198eef66eaf21f.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "cherryʙᴏᴛ")
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
