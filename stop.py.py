import asyncio
import random
from telethon import TelegramClient

api_id = 24883426  # Replace with your own API ID
api_hash = 'd7df775838ecf9e224b60430fe8452da'  # Replace with your own API Hash
phone_number = 'YOUR_PHONE_NUMBER'  # Replace with your phone number


class Account:
    def __init__(self):
        self.session_file = f'session_{phone_number}.session'
        self.client = TelegramClient(self.session_file, api_id, api_hash)
        self.stop_hunting = False

    async def start_hunting(self):
        async with self.client:
            bot_entity = await self.client.get_entity('@HeXamonbot')
            while not self.stop_hunting:
                last_messages = await self.client.get_messages(bot_entity, limit=2)
                shiny_found = any('✨ Shiny pokemon found!' in message.message.lower() for message in last_messages)
                if shiny_found:
                    self.stop_hunting = True
                    print('Shiny Pokemon found in last messages!')
                    break

                for message in last_messages:
                    await self.handle_message(message)

                if not self.stop_hunting:
                    await self.client.send_message('@HeXamonbot', '/hunt')
                gap = random.randint(2, 6)
                await asyncio.sleep(gap)

    async def handle_message(self, message):
        stop_keywords = [
            "A wild Cosmoem", "A wild Necrozma", "A wild Cosmog", "A wild Magearna", "A wild Marshadow" ,"A wild Venusaur", "A wild Houndoom" , "A wild Blastoise", "A wild Beedrill", "A wild Pidgeot", "A wild Alakazam", "A wild Slowbro", "A wild Kangaskhan", "A wild Pinsir", "A wild Gyarados", "A wild Aerodactyl", "A wild Charizard ", "A wild Mewtwo ", "A wild Ampharos", "A wild Steelix", "A wild Scizor", "A wild Heracross", "A wild Tyranitar", "A wild Sceptile", "A wild Blaziken", "A wild Swampert", "A wild Gardevoir", "A wild Sableye", "A wild Mawile", "A wild Aggron", "A wild Medicham", "A wild Manectric", "A wild Sharpedo", "A wild Camerupt", "A wild Altaria", "A wild Banette", "A wild Absol", "A wild Glalie", "A wild Salamence", "A wild Metagross", "A wild Latias", "A wild Latios", "A wild Rayquaza", "A wild Lopunny", "A wild Garchomp", "A wild Lucario", "A wild Abomasnow", " A wild Gengar" , "A wild Gallade", "A wild Regigigas", "A wild Giratina" , "A wild Arceus" , "A wild Deoxys" , "A wild Zekrom" , "A wild Kyurem" , "A wild Reshiram" , "A wild Dialga" , "A wild Genesect" , "A wild Palkia" , "A wild Kyogre" , "A wild Groudon" , "A wild Lugia" , "A wild Ho-oh" , "A wild Moltres", "A wild Zirachi", "A wild Hoopa" , "A wild Thundurus" ,"A wild Tornadus" , "A wild Cobalion" , "A wild Keldeo" , "A wild Latias" ,"A wild Latios" , "A wild Rayquaza " , "A wild Terracion" , "A wild Darkai" , "A wild Cresslia" , "A wild Landorus" , "Daily hunt limit reached" , "✨ Shiny pokemon found!" ,
        ]
        
        if any(keyword in message.message for keyword in stop_keywords):
            self.stop_hunting = True
            print(f"Found stopping keyword in message: {message.message}")
        #elif '/hunt' in message.message:
           # self.stop_hunting = True
            print("Restarting script on '/hunt' command...")
        else:
            print(f"Received message: {message.message}")

    async def connect(self):
        await self.client.start()
        # Handle OTP and TFA code if required
        # Your code logic here

    def close(self):
        self.stop_hunting = True
        self.client.disconnect()


async def main():
    account = Account()
    await account.connect()

    while not account.stop_hunting:
        await account.start_hunting()

    account.close()
    print("Script stopped.")


if __name__ == "__main__":
    asyncio.run(main())
