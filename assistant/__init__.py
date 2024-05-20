from telethon import Button, custom

from plugins import ATRA_COL, InlinePlugin
from pyUltroid import *
from pyUltroid import _ult_cache
from pyUltroid._misc import owner_and_sudos
from pyUltroid._misc._assistant import asst_cmd, callback, in_pattern
from pyUltroid.fns.helper import *
from pyUltroid.fns.tools import get_stored_file
from strings import get_languages, get_string

OWNER_NAME = blade_x_userbot_cmd.full_name
OWNER_ID = blade_x_userbot_cmd.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException as er:
        LOGS.exception(er)
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
