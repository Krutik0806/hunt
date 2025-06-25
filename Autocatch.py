import asyncio
import random
from telethon import TelegramClient, events
from telethon.errors import MessageIdInvalidError
from collections import deque

api_id = 8447214
api_hash = '9ec5782ddd935f7e2763e5e49a590c0d'

# Ask for the phone number
phone_number = input("Please enter your phone number: ")

clicked_4th_button = False
last_two_messages = deque(maxlen=2)

async def main():
    client = TelegramClient('your_session_file.session', api_id, api_hash)

    # Connect and sign in
    await client.start(phone=phone_number)

    @client.on(events.NewMessage(from_users=572621020))
    async def handle_message(event):
        global clicked_4th_button
        try:
            if event.is_private:
                # Update last two messages
                last_two_messages.append(event.raw_text)

                # Check for shiny Pokémon
                if "✨ Shiny pokemon found!" in last_two_messages:
                    print("Shiny Pokémon found! Stopping the script.")
                    await client.disconnect()

                # Handle HP messages
                hp = None
                for line in event.raw_text.split("\n"):
                    if "HP" in line:
                        hp = int(line.split("HP")[1].split("/")[0].strip())
                        print(f"HP value: {hp}")
                        break

                if hp:
                    if hp > 60:
                        await asyncio.sleep(1)
                        await event.click(random.randint(0, 3))
                    elif hp <= 60 and not clicked_4th_button:
                        await asyncio.sleep(1)
                        await event.click(4)
                        await asyncio.sleep(1)
                        await event.click(2)
                        clicked_4th_button = True

                # Handle catching events
                if "escaped" in event.raw_text or "fainted" in event.raw_text:
                    await asyncio.sleep(1)
                    await event.client.send_message(572621020, "/hunt")
                    clicked_4th_button = False

        except (asyncio.TimeoutError, MessageIdInvalidError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unhandled error: {e}")

    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
