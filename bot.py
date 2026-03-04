from pyrogram import Client, filters
from pyrogram.types import Message

api_id = 30772700
api_hash = "8ed9d78e2b9fbf8a76f5efe2dc543530"
bot_token = "8683032535:AAGsKlmx0Avd2QHjZ3fiz0BRF35_8phbt58"

app = Client("movie_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

FILE_ID = "BAACAgUAAxkBAAMaaae5hfJGo5PVZggJwHqCfqQyw3YAAm0bAAJsOEFV0EtznFsVU74eBA"

@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_video(FILE_ID)

app.run()

