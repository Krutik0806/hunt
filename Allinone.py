import asyncio
import random
from collections import deque
from telethon import TelegramClient, events
from telethon.errors import MessageIdInvalidError

# API configuration
api_id = 8447214  # Replace with your actual API ID
api_hash = '9ec5782ddd935f7e2763e5e49a590c0d'  # Replace with your actual API hash
phone_number = 'YOUR_PHONE_NUMBER'  # Replace with your phone number
session_file = f'session_{phone_number}.session'

# Initialize the client
client = TelegramClient(session_file, api_id, api_hash)

# Global flags and variables
caught_pokemon_list = ["Axew", "Shelmet", "Dwebble", "Buneary", "Lillipup", "Timburr", "Kyurem", "Slakoth", "Karrablast", "Sandile", "Darmanitan", "Scraggy", "Basculin", "Zorua"]  # List of Pokémon to catch
clicked_4th_button = False  # To track the 4th button click status
last_two_messages = deque(maxlen=2)  # To store the last two messages for shiny check
stop_hunting = False  # Flag to stop hunting if a shiny appears

# Pokéballs that can be used
pokeballs = ["Pokéball", "Great Ball", "Ultra Ball", "Master Ball"]

# Function to check for shiny Pokémon
def check_for_shiny(messages):
    for message in messages:
        if "✨ Shiny pokemon found!" in message:
            return True
    return False

# Function to select a Pokéball dynamically
async def select_pokeball():
    # Dynamically choose which ball to use, e.g., random choice or based on logic
    pokeball_choice = random.choice(pokeballs)
    print(f"Selected Pokéball: {pokeball_choice}")
    return pokeball_choice

# Function to handle incoming messages
@client.on(events.NewMessage(from_users=572621020))
async def handle_message(event):
    global clicked_4th_button, last_two_messages, stop_hunting

    try:
        # Update the last two messages deque
        last_two_messages.append(event.raw_text)

        # Check if shiny Pokémon is found
        shiny_found = check_for_shiny(last_two_messages)
        if shiny_found:
            print("Shiny Pokémon found! Stopping the script.")
            stop_hunting = True
            await client.disconnect()  # Disconnect to stop the script

        if event.is_private and "HP" in event.raw_text:
            hp = None
            for line in event.raw_text.split("\n"):
                if "HP" in line:
                    hp = int(line.split("HP")[1].split("/")[0].strip())
                    print(f"HP value: {hp}")
                    break

            if hp is not None:
                selected_ball = await select_pokeball()  # Select a Pokéball dynamically
                await asyncio.sleep(1)
                # Simulate clicking the Pokéball choice (modify as per actual button index)
                pokeball_index = pokeballs.index(selected_ball)  # Get index of the selected Pokéball
                await event.click(pokeball_index)

    except (asyncio.TimeoutError, MessageIdInvalidError):
        pass

# Event handler for catching Pokémon in the list
@client.on(events.NewMessage(from_users=572621020))
async def handle_pokemon(event):
    global clicked_4th_button, stop_hunting

    if stop_hunting:
        return

    if event.is_private and "A wild" in event.raw_text:
        poke_name = event.raw_text.split("A wild ")[-1].split(" ")[0]
        
        if poke_name in caught_pokemon_list:
            # Pokémon is in the list, catch it
            await asyncio.sleep(1)
            clicked_4th_button = False
            await event.click(0)  # Catch the Pokémon
        else:
            # Pokémon is not in the list, use Auto Kill logic
            await asyncio.sleep(1)
            await event.client.send_message(572621020, "/hunt")  # Proceed to hunt for another Pokémon
            clicked_4th_button = False

# Event handler for shiny Pokémon detection
@client.on(events.MessageEdited(from_users=572621020))
async def handle_shiny(event):
    global stop_hunting
    if event.is_private and "✨ Shiny pokemon found!" in event.raw_text:
        stop_hunting = True
        print("Shiny Pokémon detected. Stopping the script.")
        await client.disconnect()

# Main function to start the hunting process
async def start_hunting():
    async with client:
        while not stop_hunting:
            await asyncio.sleep(random.randint(2, 6))  # Random delay between hunts
            await client.send_message(572621020, "/hunt")  # Send hunt command

async def main():
    await client.start(phone=phone_number.strip())  # Start the client with phone number
    print(f"Logged in as {phone_number}")
    
    await start_hunting()  # Begin hunting
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
