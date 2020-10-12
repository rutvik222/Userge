# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.
from telethon import TelegramClient
import asyncio
import time
from telethon import events
import aiohttp

from userge import userge, Message

LOG = userge.getLogger(__name__)  # logger object
CHANNEL = userge.getCLogger(__name__)  # channel logger object


@userge.on_cmd("dic", about={
    'header': "English Dictionary-telegram",
    'usage': "{tr}dic [word]",
    'examples': 'word : Search for any word'})

client = TelegramClient('Username', api_id, api_hash)

message = 'Hey, I will be at a retreat until Saturday. I promise to get in touch as soon as I can. See you.'

def main():

    client.start()
    
    @client.on(events.NewMessage(incoming=True))
    async def _(event):
        if event.is_private:
            time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            await client.send_message(event.message.from_id, message)
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
