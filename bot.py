"""
userbot for myself
"""
from telethon import TelegramClient
from schedule import every, repeat, run_pending
import time

## stole from cc
api_id = 2134545 
api_hash = '17b514a71050f7eba50c23e79fe05e1e'
"""
delete messages from groups 
"""
async def delete_messages(client):
    excluded_group_ids = [-1001773572820, -1001407739187, -1001160694624] ##groups which I hope to remain my messages
    groups = [ dialog async for dialog in client.iter_dialogs() 
        if dialog.is_group and (not dialog.id in excluded_group_ids)]
    for group in groups:
        messages = client.iter_messages(group, from_user = 'me')
        async for message in messages:
            await message.delete()

@repeat(every(3).days)
def run_task():
    with TelegramClient('anon', api_id, api_hash) as client:
        client.loop.run_until_complete(delete_messages(client))

def start():
    while True:
        run_pending()
        time.sleep(1)

start()
