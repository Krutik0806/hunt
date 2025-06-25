import asyncio
import random
from telethon import TelegramClient

# Shared API ID and API Hash for all accounts
api_id = 24561470  # Replace with your own API ID
api_hash = '1e2d3c0c1fd09ae41a710d2daea8374b'  # Replace with your own API Hash

# List of phone numbers for different accounts
phone_numbers = [
    "+91 9712296993",  # Replace with your phone number
    "+91 7990427502",
    "+91 8799362140", # Replace with another phone number
    # Add more phone numbers as needed
]

# Generate account configurations based on the list of phone numbers
accounts_config = [
    {
        "api_id": api_id,
        "api_hash": api_hash,
        "phone_number": phone_number
    }
    for phone_number in phone_numbers
]


class Account:
    def __init__(self, api_id, api_hash, phone_number):
        self.session_file = f'session_{phone_number}.session'
        self.client = TelegramClient(self.session_file, api_id, api_hash)
        self.stop_hunting = False

    async def start_hunting(self):
        async with self.client:
            bot_entity = await self.client.get_entity('@HeXamonbot')
            while not self.stop_hunting:
                # Fetch the last 100 messages from the bot
                last_messages = []
                async for message in self.client.iter_messages(bot_entity, limit=2):
                    last_messages.append(message)

                # Check if "✨ Shiny Pokémon found!" is in any of the messages
                shiny_found = any('✨ Shiny Pokémon found!' in message.message for message in last_messages)
                if shiny_found:
                    self.stop_hunting = True
                    print(f'Shiny Pokémon found! Stopping the bot for {self.session_file}...')
                    break

                # Process the messages
                for message in last_messages:
                    await self.handle_message(message)

                # Continue hunting if not stopped
                if not self.stop_hunting:
                    await self.client.send_message('@HeXamonbot', '/hunt')

                # Random delay between hunts
                gap = random.randint(2, 6)
                await asyncio.sleep(2)

    async def handle_message(self, message):
        # List of keywords to stop the hunting
        stop_keywords = [
            "✨ Shiny Pokémon found!"
        ]
        # Check if any stopping keyword is in the message
        if any(keyword in message.message for keyword in stop_keywords):
            self.stop_hunting = True
            print(f"Stopping hunting for {self.session_file} due to message: {message.message}")
        else:
            print(f"Received message for {self.session_file}: {message.message}")

    async def connect(self):
        await self.client.start()

    def close(self):
        self.stop_hunting = True
        self.client.disconnect()


async def start_hunting_for_all_accounts(accounts):
    tasks = []
    for config in accounts:
        account = Account(config["api_id"], config["api_hash"], config["phone_number"])
        await account.connect()
        task = asyncio.create_task(account.start_hunting())
        tasks.append(task)

    # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    # Close all account connections
    for task in tasks:
        task.get_coro().cr_frame.f_locals['self'].close()

    print("All accounts have stopped hunting.")


async def main():
    await start_hunting_for_all_accounts(accounts_config)


if __name__ == "__main__":
    asyncio.run(main())
