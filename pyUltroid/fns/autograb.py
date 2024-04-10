import os
import asyncio
import requests
import re
from pyrogram import Client, filters

𝘾𝙤𝙡𝙡𝙚𝙘𝙩_𝙮𝙤𝙪𝙧_𝙝𝙪𝙨𝙗𝙖𝙣𝙙𝙤𝙨 = 1964681186
Hunt_Your_Waifu = 6816539294
Hunt_Your_Husbando = 6704987954

database_bot = 6355945378


@app.on_message(filters.user(database_bot))
async def database_bot(client, message):
    try:
        # Check if the message contains the phrase "Copy string"
        if "Copy-String:" in message.text:
            # Extract the copy string
            copy_string = message.text.split("Copy-String:")[-1].strip()
            # Reply to the message using the extracted copy string
            sent_message = await client.send_message(message.chat.id, copy_string)
            await asyncio.sleep(3)
            await sent_message.delete()
    except Exception as e:
        print(f"Error replying to {database_bot}: {e}")


@app.on_message(filters.user(𝘾𝙤𝙡𝙡𝙚𝙘𝙩_𝙮𝙤𝙪𝙧_𝙝𝙪𝙨𝙗𝙖𝙣𝙙𝙤𝙨))
async def 𝘾𝙤𝙡𝙡𝙚𝙘𝙩_𝙮𝙤𝙪𝙧_𝙝𝙪𝙨𝙗𝙖𝙣𝙙𝙤𝙨(client, message):
    try:
        reply_text = "/waifu@collect_waifu_cheats_bot"
        sent_message = await message.reply(reply_text)
        await asyncio.sleep(1)
        await sent_message.delete()
    except Exception as e:
        print(f"Error replying to {𝘾𝙤𝙡𝙡𝙚𝙘𝙩_𝙮𝙤𝙪𝙧_𝙝𝙪𝙨𝙗𝙖𝙣𝙙𝙤𝙨}: {e}")



@app.on_message(filters.user(Hunt_Your_Waifu))
async def Hunt_Your_Waifu(client, message):
    try:
        reply_text = "/waifu@collect_waifu_cheats_bot"
        sent_message = await message.reply(reply_text)
        await asyncio.sleep(1)
        await sent_message.delete()
    except Exception as e:
        print(f"Error replying to {Hunt_Your_Waifu}: {e}")


@app.on_message(filters.user(Hunt_Your_Husbando))
async def Hunt_Your_Husbando(client, message):
    try:
        reply_text = "/waifu@collect_waifu_cheats_bot"
        sent_message = await message.reply(reply_text)
        await asyncio.sleep(2)
        await sent_message.delete()
    except Exception as e:
        print(f"Error replying to {Hunt_Your_Husbando}: {e}")
