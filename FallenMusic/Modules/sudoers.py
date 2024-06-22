# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from FallenMusic import SUDOERS, app


@app.on_message(filters.command(["addsudo"]) & filters.user(OWNER_ID))
async def sudoadd(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(
                "» ʀᴇᴘʟʏ ᴜsᴇʀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ / ᴜsᴇʀ ɪᴅ."
            )
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if int(user.id) in SUDOERS:
            return await message.reply_text(f"» {user.mention} sᴜᴅᴀʜ ᴍᴀsᴜᴋ sᴜᴅᴏ ʟɪsᴛ.")
        try:
            SUDOERS.add(int(user.id))
            await message.reply_text(f"ʙᴇʀʜᴀsɪʟ {user.mention} ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴜᴅᴏ ʟɪsᴛ.")
        except:
            return await message.reply_text("ɢᴀɢᴀʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴜᴅᴏ.")

    if message.reply_to_message.from_user.id in SUDOERS:
        return await message.reply_text(
            f"» {message.reply_to_message.from_user.mention} sᴜᴅᴀʜ ᴍᴀsᴜᴋ sᴜᴅᴏ ʟɪsᴛ."
        )
    try:
        SUDOERS.add(message.reply_to_message.from_user.id)
        await message.reply_text(
            f"ʙᴇʀʜᴀsɪʟ {message.reply_to_message.from_user.mention} ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴜᴅᴏ ʟɪsᴛ."
        )
    except:
        return await message.reply_text("ɢᴀɢᴀʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴜᴅᴏ.")


@app.on_message(filters.command(["delsudo", "rmsudo"]) & filters.user(OWNER_ID))
async def sudodel(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(
                "» ʀᴇᴘʟʏ ᴜsᴇʀ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴ ᴜsᴇʀɴᴀᴍᴇ / ᴜsᴇʀ ɪᴅ."
            )
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if int(user.id) not in SUDOERS:
            return await message.reply_text(
                f"» {user.mention} ʙᴜᴋᴀɴ ᴛᴇʀᴍᴀsᴜᴋ sᴜᴅᴏ ʟɪsᴛ."
            )
        try:
            SUDOERS.remove(int(user.id))
            return await message.reply_text(
                f"» ᴍᴇɴɢʜᴀᴘᴜs {user.mention} ᴅᴀʀɪ ʟɪsᴛ sᴜᴅᴏ."
            )
        except:
            return await message.reply_text(f"ɢᴀɢᴀʟ ᴍᴇɴɢʜᴀᴘᴜs sᴜᴅᴏ.")
    else:
        user_id = message.reply_to_message.from_user.id
        if int(user_id) not in SUDOERS:
            return await message.reply_text(
                f"» {message.reply_to_message.from_user.mention} ʙᴜᴋᴀɴ ᴛᴇʀᴍᴀsᴜᴋ sᴜᴅᴏ ʟɪsᴛ."
            )
        try:
            SUDOERS.remove(int(user_id))
            return await message.reply_text(
                f"» ʀᴇᴍᴏᴠᴇᴅ {message.reply_to_message.from_user.mention} ғʀᴏᴍ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ."
            )
        except:
            return await message.reply_text(f"ɢᴀɢᴀʟ ᴍᴇɴɢʜᴀᴘᴜs ʟɪsᴛ sᴜᴅᴏ.")


@app.on_message(filters.command(["sudolist", "sudoers", "sudo"]))
async def sudoers_list(_, message: Message):
    hehe = await message.reply_text("» ᴍᴇɴɢᴀᴍʙɪʟ ʟɪsᴛ sᴜᴅᴏ...")
    text = "<u> **ᴏᴡɴᴇʀ :**</u>\n"
    count = 0
    user = await app.get_users(OWNER_ID)
    user = user.first_name if not user.mention else user.mention
    count += 1
    text += f"{count}➤ {user}\n"
    smex = 0
    for user_id in SUDOERS:
        if user_id != OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += "\n<u>✨ **sᴜᴅᴏᴇʀs :**</u>\n"
                count += 1
                text += f"{count}➤ {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text("» ᴛɪᴅᴀᴋ ᴀᴅᴀ sᴜᴅᴏ ᴜsᴇʀ.")
    else:
        await hehe.edit_text(text)
