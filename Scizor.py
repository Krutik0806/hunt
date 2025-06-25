import asyncio
import random
from telethon import TelegramClient

api_id = 24561470  # Replace with your own API ID
api_hash = '1e2d3c0c1fd09ae41a710d2daea8374b'  # Replace with your own API Hash
phone_numbers = ['+91 6355564704', '+91 9712296993', '+91 8799362140', '+91 7990427502']  # Replace with your phone numbers


class Account:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.session_file = f'session_{phone_number}.session'
        self.client = TelegramClient(self.session_file, api_id, api_hash)
        self.stop_hunting = False

    async def start_hunting(self):
        async with self.client:
            bot_entity = await self.client.get_entity('@HeXamonbot')
            while not self.stop_hunting:
                last_messages = await self.client.get_messages(bot_entity, limit=2)
                shiny_found = any('✨ shiny pokémon found!' in message.message.lower() for message in last_messages)
                if shiny_found:
                    self.stop_hunting = True
                    print(f'Shiny Pokémon found for {self.phone_number} in last messages!')
                    break

                for message in last_messages:
                    await self.handle_message(message)

                if not self.stop_hunting:
                    await self.client.send_message('@HeXamonbot', '/hunt')
                gap = random.randint(2, 6)
                await asyncio.sleep(gap)

    async def handle_message(self, message):
        stop_keywords = ["✨ Shiny Pokémon found!"]
        if any(keyword in message.message for keyword in stop_keywords):
            self.stop_hunting = True
            print(f"Found stopping keyword for {self.phone_number} in message: {message.message}")
        else:
            print(f"Received message for {self.phone_number}: {message.message}")

    async def connect(self):
        await self.client.start()
        # Handle OTP and TFA code if required
        print(f"{self.phone_number} connected!")

    def close(self):
        self.stop_hunting = True
        self.client.disconnect()


async def main():
    accounts = [Account(phone_number) for phone_number in phone_numbers]

    tasks = []
    for account in accounts:
        await account.connect()
        tasks.append(account.start_hunting())

    # Run all hunting tasks concurrently
    await asyncio.gather(*tasks)

    # Close all accounts
    for account in accounts:
        account.close()

    print("Script stopped for all accounts.")


if __name__ == "__main__":
    asyncio.run(main())
