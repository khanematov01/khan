from telethon import TelegramClient, events
import asyncio

# Telegram API ma'lumotlari
api_id = 17100414
api_hash = 'e5a7f228295b41cebf52c2c313bc49c8'

# Telegram akkauntni ulash
client = TelegramClient('user_session', api_id, api_hash)

# Guruh linki va nomi
channel_username = 'https://t.me/uzman_gr'
group_title = "UZMAN"

# Yuboriladigan matn
auto_number = '1185409275'

async def main():
    await client.start()
    print("🚀 Bot ishga tushdi...")

    @client.on(events.NewMessage(chats=channel_username))
    async def new_message_handler(event):
        if event.chat.title == group_title and "MINI RO'ZIGRISH" in event.message.text.upper():
            await client.send_message(channel_username, auto_number, reply_to=event.message.id)
            print(f"📤 Tez javob yuborildi: {auto_number}")

    await client.run_until_disconnected()

asyncio.run(main())