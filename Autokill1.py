from telethon import TelegramClient, events
import asyncio
from telethon.errors import MessageIdInvalidError

api_id = 8447214  # Replace with your actual api_id
api_hash = '9ec5782ddd935f7e2763e5e49a590c0d'  # Replace with your actual api_hash

# Ask the user to input a single phone number
phone_number = input("Enter your phone number: ")

async def handle_client(client, phone_number):
    await client.start(phone=phone_number.strip())  # Log in with the provided phone number

    print(f'''
    
 ___                   _______            _________________                                          
|   |                /   ___   \         |______    _______|                                        
|   |               /   /   \   \               |   |                                                 
|   |              /   /__ __\   \              |   |                                                 
|   |    ___      /   ________\   \             |   |                                                 
|   |___|   |    /   /         \   \      ______|   |______                                          
\___________/   /___/           \___\    |_________________|


Logged in as {phone_number}
                                              ''') 

    @client.on(events.NewMessage(from_users=572621020))
    async def _(event):
        if "appeared" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0)  
                return
                
    @client.on(events.NewMessage(from_users=572621020))
    async def _(event):
        if "Battle begins!" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0, 0) 
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0, 0)
                return
            
    @client.on(events.NewMessage(from_users=572621020))
    async def _(event):
        if "An expert trainer has challenged you to a battle." in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0, 0) 
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0, 0)
                return

    @client.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        if "used" in event.raw_text:
            try:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0, 0)  
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass
                
    @client.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        if "missed" in event.raw_text:
            try:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0, 0)  
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass
                
    @client.on(events.NewMessage(from_users=572621020))
    async def _(event):
        if "appeared" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)  # Add a delay of 0.5 seconds
                await event.click(0) 
                return
          
    @client.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        try:
            if "fainted" in event.raw_text:
               await asyncio.sleep(1)  # Add a delay of 1 second
               await event.client.send_message(572621020, "/hunt")
        except (asyncio.TimeoutError, MessageIdInvalidError):
            pass

    @client.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        try:
            if "fled" in event.raw_text:
                await asyncio.sleep(1)  # Add a delay of 1 second
                await event.client.send_message(572621020, "/hunt")
        except (asyncio.TimeoutError, MessageIdInvalidError):
            pass
     
    await client.run_until_disconnected()


async def main():
    # Create a client for the single phone number
    client = TelegramClient(f'session_{phone_number}', api_id, api_hash)

    # Handle the client
    await handle_client(client, phone_number)

asyncio.run(main())
