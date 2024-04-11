from telethon import TelegramClient, events

# String session setup
string_session = 'YOUR_STRING_SESSION'

# Telethon client setup
client = TelegramClient(string_session, api_id, api_hash)

# Forwarding messages from bots to the database bot
@client.on(events.NewMessage(from_id=BOT_ID_HERE))
async def forward_to_database_bot(event):
    # Forward the message to the database bot
    await event.forward_to('DATABASE_BOT_USERNAME_HERE')

# Copying name from forwarded message and pasting it back
@client.on(events.NewMessage)
async def handle_new_message(event):
    # Check if the message is a forwarded message from the database bot
    if event.forward:
        # Extract name from the forwarded message
        name = extract_name_from_string(event.message.text)

        # Paste the name back into the original chat
        await event.reply(name)
