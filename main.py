from telethon import TelegramClient, events
import re
import os

API_ID = 36818170
API_HASH = "ed0c8a17ef1ba8aa208075b2c9f5da91"
PHONE = "+917758005704"
SOURCE_CHANNEL = -1001003931481200
TARGET_CHANNEL = -1001003974934647

OLD_LINKS = ["https://lkbz.pro/ab29"]
NEW_LINK = "https://lkiv.cc/9d4153e1"
OLD_IDS = ["@KaranJet","https://t.me/KaranJet","t.me/KaranJet"]
NEW_ID = "@jetadda_bot"
OLD_PROMO = "K321"
NEW_PROMO = "JETADDA"
OLD_NAME = "Karan"
NEW_NAME = "JET ADDA"

client = TelegramClient("session", API_ID, API_HASH)

def process(text):
    if not text:
        return ""
    for l in OLD_LINKS:
        text = text.replace(l, "|||REG|||")
    for i in OLD_IDS:
        text = text.replace(i, "|||TG|||")
    text = re.sub(r'https?://lkbz[^\s]+', '', text)
    text = re.sub(r'https?://[^\s]+', '', text)
    text = re.sub(r't\.me/[^\s]+', '', text)
    text = text.replace("|||REG|||", NEW_LINK)
    text = text.replace("|||TG|||", NEW_ID)
    text = text.replace(OLD_PROMO, NEW_PROMO)
    text = text.replace("Karan 2.0 🚀", NEW_NAME)
    text = text.replace("Karan", NEW_NAME)
    text = re.sub(r'@KaranJet', NEW_ID, text, flags=re.IGNORECASE)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    try:
        msg = event.message
        text = process(msg.text or msg.message or "")
        if msg.photo:
            await client.send_file(TARGET_CHANNEL, msg.photo, caption=text or None)
        elif msg.video:
            await client.send_file(TARGET_CHANNEL, msg.video, caption=text or None)
        elif msg.document:
            await client.send_file(TARGET_CHANNEL, msg.document, caption=text or None)
        elif msg.audio:
            await client.send_file(TARGET_CHANNEL, msg.audio, caption=text or None)
        elif msg.voice:
            await client.send_file(TARGET_CHANNEL, msg.voice)
        elif msg.sticker:
            await client.send_file(TARGET_CHANNEL, msg.sticker)
        elif msg.gif:
            await client.send_file(TARGET_CHANNEL, msg.gif, caption=text or None)
        elif msg.video_note:
            await client.send_file(TARGET_CHANNEL, msg.video_note)
        elif text:
            await client.send_message(TARGET_CHANNEL, text)
        print("✅ Forwarded!")
    except Exception as e:
        print(f"❌ Error: {e}")

print("🚀 Starting...")
with client:
    client.start(phone=PHONE)
    print("✅ LIVE!")
    client.run_until_disconnected()
