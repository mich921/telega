from telethon import TelegramClient

api_id = 1
api_hash = '1'

client = TelegramClient('+79201462710', api_id, api_hash)


async def qwer():
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if not dialog.message.out:
            try:
                print(f'сообщение от {dialog.entity.first_name}: \n"{dialog.message.message}"')
            except Exception as e:
                pass


with client:
    client.loop.run_until_complete(qwer())
