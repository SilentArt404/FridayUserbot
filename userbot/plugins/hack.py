from telethon import events
import asyncio
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"hack", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 11)
    input_str = event.pattern_match.group(1)
    rip = await edit_or_reply(event, "`Searching For Users Data Folder 📂`"
    animation_chars = [
    "`Data Found! Starting Hack.`",
    "`Please Wait. Starting Termal....`",
    "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
    "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
    "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
    "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
    "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
    "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
    "`Hacking... 84%\n█████████████████████▒▒▒▒ `",
    "`Hacking... 100%\n███████████████████████`",
    "`Hacking Sucessfull ! Now Please Wait ! Exporting Data...... `"
    "`Exporting Data To userbot/plugins/hackdata`..."
    "`Export Complete. Now Check Your Folder 📂`"
    ]
    for i in animation_ttl:
                await asyncio.sleep(animation_interval)
                await rip.edit(animation_chars[i % 11])
    else:
        await event.edit("No User is Defined\n are u dumb\n reply to a user.")
