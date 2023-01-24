from db_operations import get_all_phones
from telethon import TelegramClient

list_api_id, list_api_hash, list_phone = get_all_phones()

for api_id, api_hash, phone in zip(list_api_id, list_api_hash, list_phone):

    client = TelegramClient(phone, api_id, api_hash)


    async def qwer():
        dialogs = await client.get_dialogs()
        for dialog in dialogs:
            if not dialog.message.out:
                try:
                    if dialog.entity.first_name != 'Telegram' and dialog.entity.first_name != 'Я':
                        print(f'Ну шо, мне({phone}) пришло сообщение от {dialog.entity.first_name}: \n"{dialog.message.message}"\n\n\n')
                        pass
                except Exception as e:
                    print(e)


    with client:
        client.loop.run_until_complete(qwer())
