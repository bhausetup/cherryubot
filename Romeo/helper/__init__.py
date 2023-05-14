import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "cherry"])

async def join(client):
    try:
        await client.join_chat("@AdulT_R00M")
    except BaseException:
        pass
