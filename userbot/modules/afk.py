from time import time
from userbot import CB
from userbot.core.helpers.utils import get_arg
from userbot.core.helpers.database import set_vars, get_vars, remove_vars

__MODULE__ = "afk"
__HELP__ = """
<b>『 bantuan untuk afk 』</b>

  <b>• perintah:</b> <code>{0}afk</code>
  <b>• penjelasan:</b> untuk mengaktifkan afk 

  <b>• perintah:</b> <code>{0}unafk</code>
  <b>• penjelasan:</b> untuk menonaktifkan afk
"""


async def get_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    if days > 0:
        return f"{days} hari {hours} jam {minutes} menit"
    elif hours > 0:
        return f"{hours} jam {minutes} menit"
    elif minutes > 0:
        return f"{minutes} menit {seconds} detik"
    else:
        return f"{seconds} detik"


class awayFromKeyboard:
    def __init__(self, client, message, reason=""):
        self.client = client
        self.message = message
        self.reason = reason

    async def set_afk(self):
        db_afk = {"time": time(), "reason": self.reason}
        msg_afk = (
            f"<b>❏ sedang afk\n ╰ alasan: {self.reason}</b>"
            if self.reason
            else "<b>❏ sedang afk</b>"
        )
        await set_vars(self.client.me.id, "AFK", db_afk)
        await self.message.reply(msg_afk, disable_web_page_preview=True)
        return await self.message.delete()

    async def get_afk(self):
        vars = await get_vars(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("time")
            afk_reason = vars.get("reason")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = (
                f"<b>❏ sedang afk\n ├ waktu: {afk_runtime}\n ╰ alasan: {afk_reason}</b>"
                if afk_reason
                else f"<b>❏ sedang afk\n ╰ waktu: {afk_runtime}</b>"
            )
            return await self.message.reply(afk_text, disable_web_page_preview=True)

    async def unset_afk(self):
        vars = await get_vars(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("time")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = f"<b>❏ kembali online\n ╰ afk selama: {afk_runtime}</b>"
            await self.message.reply(afk_text)
            await self.message.delete()
            return await remove_vars(self.client.me.id, "AFK")


@CB.UBOT("afk")
async def _(client, message):
    reason = get_arg(message)
    afk_handler = awayFromKeyboard(client, message, reason)
    await afk_handler.set_afk()


@CB.AFK(True)
async def _(client, message):
    afk_handler = awayFromKeyboard(client, message)
    await afk_handler.get_afk()


@CB.UBOT("unafk")
async def _(client, message):
    afk_handler = awayFromKeyboard(client, message)
    return await afk_handler.unset_afk()

