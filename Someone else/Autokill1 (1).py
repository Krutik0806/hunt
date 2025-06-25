from telethon import TelegramClient, events
import asyncio
import random

# Your Telegram API credentials
api_id = 8447214  # Replace with your actual api_id
api_hash = '9ec5782ddd935f7e2763e5e49a590c0d'  # Replace with your actual api_hash

# List of phone numbers for multiple accounts
phone_numbers = [
    "+91 8799362140",
    "+91 9712296993",
    "+91 7990427502"
]

# Global flags and counters
stop_hunting = False
pokemons_killed = 0
expert_trainers_encountered = 0


async def wait_for_event(client, event_type, timeout=5):
    """
    Waits for a specific event with a timeout.
    """
    event_future = asyncio.Future()

    @client.on(event_type)
    async def listener(event):
        if not event_future.done():
            event_future.set_result(event)

    try:
        return await asyncio.wait_for(event_future, timeout=timeout)
    except asyncio.TimeoutError:
        return None
    finally:
        client.remove_event_handler(listener, event_type)


async def handle_client(client, phone_number):
    global stop_hunting, pokemons_killed, expert_trainers_encountered
    await client.start(phone=phone_number.strip())  # Log in with the provided phone number

    print(f"Logged in as {phone_number}")

    @client.on(events.NewMessage(from_users=572621020))
    async def handle_shiny_pokemon(event):
        global stop_hunting
        if "✨ Shiny Pokémon found!" in event.raw_text:
            print(f"Shiny Pokémon found by {phone_number}! Stopping actions.")
            stop_hunting = True
            return

    @client.on(events.NewMessage(from_users=572621020))
    async def handle_appearance(event):
        global stop_hunting
        if stop_hunting:
            return
        if "appeared" in event.raw_text and event.buttons:
            await asyncio.sleep(0.5)
            await event.click(0, 0)

    @client.on(events.NewMessage(from_users=572621020))
    async def handle_trainer_skip(event):
        global stop_hunting, expert_trainers_encountered
        if stop_hunting:
            return
        if "An expert trainer has challenged you to a battle." in event.raw_text:
            expert_trainers_encountered += 1
            print(f"Expert trainer encountered by {phone_number}. Total so far: {expert_trainers_encountered}")
            await asyncio.sleep(1)
            await event.client.send_message(572621020, "/hunt")

    @client.on(events.MessageEdited(from_users=572621020))
    async def handle_flee_or_hunt(event):
        global stop_hunting, pokemons_killed
        if stop_hunting:
            return
        if "fled" in event.raw_text or "fainted" in event.raw_text:
            pokemons_killed += 1
            print(f"Pokémon killed by {phone_number}. Total so far: {pokemons_killed}")
            await asyncio.sleep(1)
            await event.client.send_message(572621020, "/hunt")

    @client.on(events.NewMessage(from_users=572621020))
    async def handle_battle(event):
        global stop_hunting
        if stop_hunting:
            return
        if "Battle begins!" in event.raw_text and event.buttons:
            while True:
                try:
                    # Avoid the first button for the specific account
                    if phone_number == "+91 7990427502":
                        random_button = random.randint(1, min(len(event.buttons[0]) - 1, 3))
                    else:
                        random_button = random.randint(0, min(len(event.buttons[0]) - 1, 3))

                    print(f"Selecting button {random_button + 1} in battle for {phone_number}")
                    await asyncio.sleep(0.5)
                    await event.click(0, random_button)

                    # Wait for the next event to check if battle ended
                    response_event = await wait_for_event(client, events.MessageEdited(from_users=572621020), timeout=5)
                    if response_event and "fainted" in response_event.raw_text:
                        print(f"Battle ended for {phone_number}.")
                        break
                except Exception as e:
                    print(f"Error during battle for {phone_number}: {e}")
                    continue

    @client.on(events.NewMessage(from_users=572621020))
    async def handle_hunt_timeout(event):
        global stop_hunting
        if stop_hunting:
            return
        if "/hunt" in event.raw_text:
            try:
                await asyncio.sleep(2)
                await event.client.send_message(572621020, "/hunt")
            except Exception as e:
                print(f"Error during hunt for {phone_number}: {e}")
                await event.client.send_message(572621020, "/hunt")

    await client.run_until_disconnected()


async def main():
    clients = []
    tasks = []

    for phone_number in phone_numbers:
        client = TelegramClient(f'session_{phone_number}', api_id, api_hash)
        clients.append(client)
        tasks.append(handle_client(client, phone_number))

    await asyncio.gather(*tasks)


# Run the main function
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nSummary:")
    print(f"Total Pokémon killed: {pokemons_killed}")
    print(f"Total expert trainers encountered: {expert_trainers_encountered}")
