import asyncio
import random
from telethon import TelegramClient
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

api_id = 24561470  # Replace with your own API ID
api_hash = '1e2d3c0c1fd09ae41a710d2daea8374b'  # Replace with your own API Hash
phone_number = '+91 6355564704
'  # Replace with your phone number


class Account:
    def __init__(self):
        self.session_file = f'session_{phone_number}.session'
        self.client = TelegramClient(self.session_file, api_id, api_hash)
        self.stop_hunting = False

    async def start_hunting(self):
        async with self.client:
            bot_entity = await self.client.get_entity('@ZYRA_ROBOT')
            while not self.stop_hunting:
                # Step 1: Send the /find command to encounter a monster
                await self.client.send_message(bot_entity, '/find')
                await asyncio.sleep(random.uniform(1, 3))  # Short pause for response

                # Step 2: Check the latest messages from the bot
                last_messages = [message async for message in self.client.iter_messages(bot_entity, limit=10)]
                for message in last_messages:
                    if "you encounter" in message.message.lower():
                        # Click on the "Fight" button
                        await self.click_button(bot_entity, message, "Fight")
                        await asyncio.sleep(random.uniform(1, 3))

                        # Step 3: Click on the "Attack" button after choosing to fight
                        await self.click_button(bot_entity, message, "Attack")
                        await asyncio.sleep(random.uniform(1, 3))

                    elif "defeated" in message.message.lower():
                        print("Monster defeated, finding a new one...")
                        break  # Exit the loop and start hunting again

                # Pause between hunting attempts
                gap = random.randint(2, 6)
                await asyncio.sleep(gap)

    async def click_button(self, bot_entity, message, button_text):
        if message.buttons:
            for row in message.buttons:
                for button in row:
                    if button_text.lower() in button.text.lower():
                        # Use GetBotCallbackAnswerRequest to click the inline button
                        try:
                            await self.client(GetBotCallbackAnswerRequest(
                                peer=bot_entity,
                                msg_id=message.id,
                                data=button.data
                            ))
                            print(f"Clicked on '{button_text}' button")
                            return
                        except Exception as e:
                            print(f"Failed to click '{button_text}' button: {e}")

    async def connect(self):
        await self.client.start()
        print("Connected to Telegram")

    async def close(self):
        self.stop_hunting = True
        await self.client.disconnect()
        print("Disconnected from Telegram")

async def main():
    account = Account()
    await account.connect()

    try:
        while not account.stop_hunting:
            await account.start_hunting()
    finally:
        await account.close()
        print("Script stopped.")

if __name__ == "__main__":
    asyncio.run(main())
