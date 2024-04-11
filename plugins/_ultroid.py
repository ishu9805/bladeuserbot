
from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, blade_cmd

REPOMSG = """
• **ULTROID USERBOT** •\n
• Repo - [Click Here](https://github.com/ishu9805/bladeuserbot)
• Addons - [Click Here](https://github.com/ishu9805/addons)
• Support - @Blade_x_community
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/ishu9805/bladeuserbot"),
        Button.url("Addons", "https://github.com/ishu9805/addons"),
    ],
    [Button.url("Support Group", "t.me/@Blade_x_community")],
]

ULTSTRING = """🎇 **Thanks for Deploying Ultroid Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@blade_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@blade_cmd(pattern="ultroid$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/c35b0ac3f65c9ecb329e7.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
