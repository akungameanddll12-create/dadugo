import asyncio, random, os, threading
from flask import Flask
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.getenv("API_ID", "33806675"))
API_HASH = os.getenv("API_HASH", "9e6c530980ee4f6f4a681bf8b7195861")
SESSION = os.getenv("SESSION")
MY_USERNAME = os.getenv("MY_USERNAME", "Sukma282828")
ALLOWED = "DUEL DADU GO 1+"

app = Flask('')
@app.route('/')
def home(): return "ok"
threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080), daemon=True).start()

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    try:
        chat = await event.get_chat()
        title = getattr(chat, 'title', '') or ''
    except: title = ""
    if ALLOWED not in title: return
    text = (event.message.text or "").lower()
    if "duel diterima" in text and MY_USERNAME.lower() in text:
        await asyncio.sleep(random.uniform(0.7, 1.2))
        await client.send_message(event.chat_id, "🎲")

client.start()
client.run_until_disconnected()
