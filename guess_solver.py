from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
import asyncio

api_id = 8447214
api_hash = '9ec5782ddd935f7e2763e5e49a590c0d'

# List of phone numbers for multiple accounts
phone_numbers = ['+91 7990427502']  # Replace with actual phone numbers
clients = []

# Group chat ID and owner's Telegram ID
chatid = -4563423056
ownerid = 7512169299

async def start_clients():
    for phone in phone_numbers:
        client = TelegramClient(StringSession(), api_id, api_hash)
        await client.connect()
        if not await client.is_user_authorized():
            await client.send_code_request(phone)
            print(f"Enter the code for {phone}:")
            code = input('Code: ')
            await client.sign_in(phone, code)

        clients.append(client)

        @client.on(events.NewMessage(from_users=ownerid, pattern=".bin", outgoing=True))
        async def guesser(event):
            await client.send_message(entity=chatid, message='/guess')
            for i in range(1, 3000):
                await asyncio.sleep(125)
                await client.send_message(entity=chatid, message='/guess')

        @client.on(events.NewMessage(from_users=572621020, pattern="Who's that pokemon?", chats=(int(chatid)), incoming=True))
        async def handle_pokemon_image(event):
            try:
                found = False
                for size in event.message.photo.sizes:
                    size_str = str(size) if size is not None else None
                    if size_str:
                        for file in os.listdir("cache/"):
                            with open(f"cache/{file}", 'r') as f:
                                file_content = f.read()
                            if file_content == size_str:
                                chat = await event.get_chat()
                                await client.send_message(chat, f"{(file).split('.txt')[0]}")
                                await asyncio.sleep(2)
                                await client.send_message(chat, "/guess")
                                found = True
                                break
                        if not found:
                            chat = await event.get_chat()
                            await client.send_message(chat, "not found")
                            await asyncio.sleep(70)
                            await client.send_message(chat, "/guess")
                        with open("cache.txt", 'w') as file:
                            file.write(size_str)
                    else:
                        print("Size is None. Skipping write.")
            except Exception as e:
                print(f"Unhandled exception on handle_pokemon_image: {e}")

        @client.on(events.NewMessage(from_users=572621020, pattern="The pokemon was ", chats=int(chatid)))
        async def handle_pokemon_response(event):
            try:
                pokemon_name = ((event.message.text).split("The pokemon was ")[1]).split(" ")[0]
                try:
                    with open(f"cache/{pokemon_name}.txt", 'w') as file:
                        with open("cache.txt", 'r') as inf:
                            cont = inf.read()
                            file.write(cont)
                except PermissionError as e:
                    print(f"Permission error: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")
                os.remove("cache.txt")
                chat = await event.get_chat()
                await client.send_message(chat, "/guess")
            except Exception as e:
                print(f"Unhandled exception on handle_pokemon_response: {e}")

        @client.on(events.NewMessage(pattern="Too many commands are being used", chats=int(chatid)))
        async def handle_rate_limit(event):
            print("Rate limit encountered. Sleeping for 125 seconds.")
            await asyncio.sleep(125)

        @client.on(events.NewMessage(pattern="There is already a guessing game being played", chats=int(chatid)))
        async def handle_existing_game(event):
            print("Existing guessing game encountered. Sleeping for 60 seconds.")
            await asyncio.sleep(60)

    # Start all clients
    for client in clients:
        client.start()

    # Keep the script running
    await asyncio.gather(*(client.run_until_disconnected() for client in clients))

if __name__ == "__main__":
    # Check if there's an existing event loop
    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
    except RuntimeError:
        # No current event loop, so create a new one
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # Run the asynchronous function to start the clients
    loop.run_until_complete(start_clients())

