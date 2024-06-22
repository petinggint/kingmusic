import asyncio

from pyrogram import Client, __version__ as ver


API_ID = input("\nEnter Your API ID :\n > ")
API_HASH = input("\nEnter Your API HASH :\n > ")

print("\n\nMasukkan nomor telepon yang terkait dengan akun telegram Anda ketika ditanya.\n\n")

fallen = Client("Fallen", api_id=API_ID, api_hash=API_HASH, in_memory=True)


async def main():
    await fallen.start()
    sess = await fallen.export_session_string()
    txt = f"Here is your Pyrogram {ver} String Session\n\n<code>{sess}</code>\n\nDon't share it with anyone.\nDon't forget to join @FallenAssociation"
    ok = await fallen.send_message("me", txt)
    print(f"Here is your Pyrogram {ver} String Session\n{sess}\nDouble click to copy.") 


asyncio.run(main())
