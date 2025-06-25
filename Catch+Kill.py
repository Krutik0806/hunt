import asyncio
import re
from telethon import TelegramClient, events
import random
from telethon.errors import MessageIdInvalidError

api_id = 8447214  # Replace with your actual api_id
api_hash = '9ec5782ddd935f7e2763e5e49a590c0d'  # Replace with your actual api_hash

# Define the list of Pokemon you want to catch
catch_list = ["Axew", "Shelmet", "Dwebble", "Buneary", "Lillipup", "Timburr",
              "Kyurem", "Slakoth", "Karrablast", "Sandile", "Darmanitan",
              "Scraggy", "Basculin", "Zorua"]

# Define the specific Pokeballs to use
allowed_pokeballs = ["Great Ball", "Ultra Ball"]

# Function to check if the Pokemon name is in the catch list
def is_desired_pokemon(pokemon_name):
    return pokemon_name.strip() in catch_list

async def handle_message(event):
    global clicked_4th_button
    try:
        if event.is_private and "A wild" in event.raw_text:
            pokemon_name = event.raw_text.split("appeared")[0].split()[-1]

            if is_desired_pokemon(pokemon_name):
                # Catch logic for desired Pokemon
                await asyncio.sleep(1)
                clicked_4th_button = False  # Reset the flag
                pokeball = random.choice(allowed_pokeballs)  # Choose a random allowed Pokeball
                print(f"Using {pokeball} for {pokemon_name}")  # Log the Pokeball choice

                # Retry logic for button click
                for _ in range(3):  # Try clicking the button up to 3 times
                    try:
                        await event.click(0)  # Throw the chosen Pokeball
                        break  # Exit the loop if successful
                    except telethon.errors.rpcerrorlist.DataInvalidError:
                        await asyncio.sleep(2)  # Wait before retrying

            else:
                # Kill logic for unwanted Pokemon
                await asyncio.sleep(0.5)  # Adjust delay for desired behavior
                await event.click(0)  # Run away

        elif event.is_private and "HP" in event.raw_text:
            hp = None
            for line in event.raw_text.split("\n"):
                if "HP" in line:
                    hp = int(line.split("HP")[1].split("/")[0].strip())
                    print(f"HP value: {hp}")
                    break

            if hp and hp > 60:
                await asyncio.sleep(1)
                await event.click(random.randint(0, 3))
            elif hp and hp <= 60 and not clicked_4th_button:
                await asyncio.sleep(1)
                await event.click(4)
                await asyncio.sleep(1)
                await event.click(0)
                clicked_4th_button = True

        elif event.is_private and any(keyword in event.raw_text for keyword in [
                "escaped", "ball failed and the wild", "Your entire team has fainted",
                "Expert", "Trainer", "An", "expert", "challenged", "fainted", "caught", "fled"]):
            await asyncio.sleep(1)
            await event.client.send_message(572621020, "/hunt")
            clicked_4th_button = False

        # Handle the case where there might not be four buttons
        elif event.is_private:
            buttons = event.buttons_flat  # Get all available buttons
            if buttons:  # Check if any buttons exist
                # Click the first button based on its text or position (if needed)
                await event.click(buttons[0].text)  # Example: click first button by text

    except (asyncio.TimeoutError, MessageIdInvalidError):
        pass

async def main():
    global clicked_4th_button
    clicked_4th_button = False  # Initialize the flag

    client = TelegramClient('your_session_file.session', api_id, api_hash)

    @client.on(events.NewMessage(from_users=572621020))
    async def _(event):
        await handle_message(event)

    @client.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        await handle_message(event)

    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
