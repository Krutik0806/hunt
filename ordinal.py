import asyncio
from telethon import TelegramClient, events
from telethon.errors import MessageIdInvalidError

api_id = 24883426
api_hash = 'd7df775838ecf9e224b60430fe8452da'
async def main():
    client = TelegramClient('session_name', api_id, api_hash)

    @client.on(events.NewMessage(from_users=5364964725))
    async def _(event):
        if "Monster" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)
                await event.click(1, 0)

    @client.on(events.NewMessage(from_users=5364964725))
    async def _(event):
        if "otherwise" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)
                await asyncio.sleep(1)
                await event.click(4)
                await event.client.send_message(-id,"Captcha Came Go And Solve")

    @client.on(events.NewMessage(from_users=5364964725))
    async def _(event):
        if "1 tries" in event.raw_text:
            await asyncio.sleep(0.5)
            await event.client.send_message(-"I Failed In Solving Captcha")
            await event.client.send_message(5364964725, "/explore")

    @client.on(events.MessageEdited(from_users=5364964725))
    async def _(event):
        if "Monster" in event.raw_text:
            try:
                await asyncio.sleep(0.5)
                await event.click(0)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    @client.on(events.MessageEdited(from_users=5364964725))
    async def _(event):
        if "Unfortunately" in event.raw_text:
            try:
                await asyncio.sleep(0.5)
                await event.click(0)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    @client.on(events.MessageEdited(from_users=5364964725))
    async def _(event):
        if "defeated" in event.raw_text:
            try:
                await asyncio.sleep(1)
                await event.client.send_message(5364964725, "/explore")
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    @client.on(events.MessageEdited(from_users=5364964725))
    async def _(event):
        if "Ops" in event.raw_text:
            try:
                await asyncio.sleep(0.5)
                await event.client.send_message(5364964725, "/explore")
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    @client.on(events.MessageEdited(from_users=5364964725))
    async def _(event):
        if "killed" in event.raw_text:
            try:
                await asyncio.sleep(0.5)
                await event.client.send_message(-1001889306146, "Captcha Solved /explore Going On")
                await event.client.send_message(5364964725, "/explore")
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    @client.on(events.NewMessage(from_users=5364964725))
    async def _(event):
        if "Level" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)
                await event.click(0)

    @client.on(events.NewMessage(from_users=5364964725))
    async def _(event):
        if "Wishing" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)
                await event.click(0)

    @client.on(events.NewMessage(from_users=5364964725))
    async def _(event):
        if "ongoing" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)
                await event.client.send_message(5364964725, "/explore")

    @client.on(events.NewMessage(from_users=5364964725))
    async def _(event):
        if "offers?" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(0.5)
                await event.click(0)

    @client.on(events.MessageEdited(from_users=5364964725))
    async def _(event):
        try:
            if "Offers you" in event.raw_text:
                per_pearl = None
                per_ticket = None
                contains_other_items = False

                for line in event.raw_text.split("\n"):
                    if "pearls for" in line:
                        per_pearl = int(line.split("for")[1].split("coins per")[0].strip())
                    elif "tickets for" in line:
                        per_ticket = int(line.split("for")[1].split("coins per")[0].strip())
                    elif any(item in line for item in ["rope", "net", "large net", "chain", "tranquilizer", "freeze ray"]):
                        contains_other_items = True

                if per_pearl and per_pearl > 230:
                    await asyncio.sleep(0.5)
                    await event.client.send_message(5364964725, "/explore")
                elif per_ticket and per_ticket > 460:
                    await asyncio.sleep(0.5)
                    await event.client.send_message(5364964725, "/explore")
                elif contains_other_items:
                    await asyncio.sleep(0.5)
                    await event.client.send_message(5364964725, "/explore")
                elif per_pearl and per_pearl <= 230:
                    await asyncio.sleep(0.5)
                    await event.click(0, 0)
                elif per_ticket and per_ticket <= 460:
                    await asyncio.sleep(0.5)
                    await event.click(0)
        except (asyncio.TimeoutError, MessageIdInvalidError):
            pass
            
    @client.on(events.NewMessage(from_users=5364964725))
    async def _(event):
        if any(keyword in event.raw_text for keyword in ["while", "Common", "Rare"]):
            await asyncio.sleep(0.5)
            await event.client.send_message(5364964725, "/explore")

    @client.on(events.MessageEdited(from_users=5364964725))
    async def _(event):
        if "traded" in event.raw_text:
            await asyncio.sleep(1)
            await event.client.send_message(5364964725, "/explore")

    @client.on(events.MessageEdited(from_users=5364964725))
    async def _(event):
        if "Epic" in event.raw_text:
             await asyncio.sleep(1)
             await event.client.send_message(-1001889306146, "pet appear")
            
    @client.on(events.MessageEdited(from_users=5364964725))
    async def _(event):
        if "Exotic"in event.raw_text:
            await client.disconnect()

    await client.start()
    await client.run_until_disconnected()

asyncio.run(main())
