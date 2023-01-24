from telethon import TelegramClient

api_id = 1
api_hash = '1'

message = 'Привет'

client = TelegramClient('+79185122780', api_id, api_hash)


async def main(target_name):
    await client.send_message(target_name, message)


with client:
    client.loop.run_until_complete(main('Tydirium_shuttle'))
