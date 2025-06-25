from telethon import TelegramClient, events
import asyncio
from telethon.errors import MessageIdInvalidError

api_id = 8447214  # Replace with your actual api_id
api_hash = '9ec5782ddd935f7e2763e5e49a590c0d'  # Replace with your actual api_hash

# Predefined list of phone numbers
phone_numbers = [
    "+1234567890",  # Replace with actual phone numbers
    "+0987654321",  # Add more phone numbers as needed
    "+1122334455"
]

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
    async def handle_new_message(event):
        if "appeared" in event.raw_text and event.buttons:
            await asyncio.sleep(0.5)
            await event.click(0)

        elif "Battle begins!" in event.raw_text and event.buttons:
            await asyncio.sleep(0.5)
            await event.click(0, 0)
            await asyncio.sleep(0.5)
            await event.click(0, 0)

        elif "An expert trainer has challenged you to a battle." in event.raw_text and event.buttons:
            await asyncio.sleep(0.5)
            await event.click(0, 0)
            await asyncio.sleep(0.5)
            await event.click(0, 0)

    @client.on(events.MessageEdited(from_users=572621020))
    async def handle_message_edited(event):
        try:
            if "used" in event.raw_text or "missed" in event.raw_text:
                await asyncio.sleep(0.5)
                await event.click(0, 0)

            elif "fainted" in event.raw_text or "fled" in event.raw_text:
                await asyncio.sleep(1)
                await event.client.send_message(572621020, "/hunt")

        except (asyncio.TimeoutError, MessageIdInvalidError):
            pass

    await client.run_until_disconnected()


async def main():
    # Create a list to hold all the clients
    clients = []

    # Initialize each client and start handling
    for phone_number in phone_numbers:
        client = TelegramClient(f'session_{phone_number.strip()}', api_id, api_hash)
        clients.append(client)
        asyncio.create_task(handle_client(client, phone_number.strip()))

    # Run all clients concurrently
    await asyncio.gather(*(client.run_until_disconnected() for client in clients))

asyncio.run(main())
