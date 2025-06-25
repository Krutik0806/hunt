from telethon import events , TelegramClient
from asyncio import sleep as zzz
from random import randint
from re import match

#dont edit else gay this constant
api_id = 2282111
api_hash = 'da58a1841a16c352a2a999171bbabcad'
bot = TelegramClient('session' , api_id , api_hash)
chat = 572621020

#edit the list
list = ["Eternatus", "Zacian", "Shaymin", "Dialga", "Palkia", "Mewtwo", "Arceus", "Zamazenta", "Glastrier", "Calyrex", "Kyurem", "Lunala", "Necrozma", "Rayquaza", "Cosmoem", "Yveltal", "Kyogre", "Xerneas", "Cosmog", "Groudon", "Giratina", "Zeraora", "Marshadow", "Buzzwole", "Solgaleo", "Zyagrde", "Regigigas", "Articuno", "Moltres", "Zapdos", "Mew", "Ho-oh", "Lugia", "Suicune", "Raikou", "Entei", "Celebi", "Deoxys", "Jirachi", "Regirock", "Registeel", "Regice", "Latios", "Latias", "Darkrai", "Azelf", "Uxie", "Mesprit", "Reshiram", "Zekrom", "Victini", "Cobalion", "Virizion", "Terrakion", "Keldeo", "Meloetta", "Hoopa", "Diancie", "Volcanion", "Pheromosa", "Magearna", "Tapu Koko", "Tapu Lele", "Tapu Fini", "Tapu Bulu", "Type: Null", "Silvally", "Guzzlord", "Kartana", "Urshifu", "Enamorus", "Regidrago", "Regieleki", "Spectrier", "Sableye", "Zarude","Venusaur", "Charizard", "Blastoise", "Beedrill", "Pidgeot", "Alakazam", "Slowbro", "Gengar", "Kangaskhan", "Pinsir", "Gyarados", "Aerodactyl", "Mewtwo", "Ampharos", "Steelix", "Scizor", "Heracross", "Houndoom", "Tyranitar", "Sceptile", "Blaziken", "Swampert", "Gardevoir", "Sableye", "Mawile", "Aggron", "Medicham", "Manectric", "Sharpedo", "Camerupt", "Altaria", "Banette", "Absol", "Glalie", "Salamence", "Metagross", "Latias", "Latios", "Rayquaza", "Lopunny", "Garchomp", "Lucario", "Abomasnow", "Gallade", "Audino", " Charmander", "Charmeleon", "Gastly", "Abra", "Kadabra", "Darmanitan", "Barraskewda", "Squirtle", "Riolu", "Bulbasaur", "Genesect","Electrike", "Mudbray", "Munchlax", "Snorlax", "Greninja", "Froakie", "Frogadier", "Primarina", "Floette", "Flabebe", "Dreepy", "Drakloak", "Incineroar", "Torracat", "Dragapult", "Inteleon", "Cinderace" , "Conkeldurr", "Golisopod", "Archaludon", "Buneary", "Mienshao", "Noivern", "Braviary", "Talonflame", "Litten", "Bisharp" , "Ninetails" , "Mienfoo", "Haunter", "Fletchling", "Fletchinder", "Dragonair", "Dratini", "Slaking", "Slakoth", "Kadabra", "Manaphy", "Kirlia", "Magnezone", "Gabite", "Drizzile", "Raboot", "Scorbunny", "Sobble", "Charmander", "Noibat", "Axew", "Fraxure", "Haxorus", "Golett", "Golurk", "Mudsdale", "Poipole", "Kubfu", "Heatran", "Volcanion", "Hawlucha", "✨", "Scraggy", "Nincada"]


@bot.on(events.NewMessage(outgoing=True,pattern='.go'))
async def begin(event):
    global hunt
    hunt = True
    x = await bot.send_message(chat , "/hunt")
    try:  
     async with bot.conversation('@Hexamonbot') as conv:
       await conv.get_response(x.id)
    except:
       await zzz(2,3)
       await bot.send_message(chat , "/hunt")
    for i in range(1,10000):
      await zzz(randint(1000, 1020))
      await bot.send_message(chat , "/hunt")

@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
    if hunt == True:
     text = event.message.text
     hun = True
     message = await bot.get_messages(chat, ids=event.message.id)
     if ("A shiny" in text):
        bot.disconnect()
     elif("TM" in text):
        print(event.message.text)
        await zzz(randint(2,3))
        x = await bot.send_message(chat , "/hunt")
        try:  
         async with bot.conversation('@Hexamonbot') as conv:
           await conv.get_response(x.id)
        except:
           await zzz(2,3)
           await bot.send_message(chat , "/hunt")
     elif any(item in text for item in list):
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
     elif("A wild" in text or "An expert" in text):
      if hun == False:
       pass
      else:
       await zzz(randint(2,5))
       x = await bot.send_message(chat , "/hunt")
       try:  
        async with bot.conversation('@Hexamonbot') as conv:
          await conv.get_response(x.id)
       except:
          await zzz(2,3)
          await bot.send_message(chat , "/hunt")
      

@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
   print(event.message.text)
   if event.message.text[:13] == "Battle begins":
        message = await bot.get_messages(chat, ids=event.message.id)
        await zzz(2)
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")      


@bot.on(events.MessageEdited(chats=chat))
async def cacther(event):
   message = await bot.get_messages(chat, ids=event.message.id)
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls") 
   if event.message.text[:4] == "Wild":
      await zzz(2)
      await message.click(text = "Ultra")
      await message.click(text = "Ultra")
      await message.click(text = "Ultra")
   if any(keyword in event.message.text for keyword in ['fled', 'fainted', 'caught']):
      await zzz(randint(2,5))
      x = await bot.send_message(chat , "/hunt")
      try:  
       async with bot.conversation('@Hexamonbot') as conv:
         await conv.get_response(x.id)
      except:
         await zzz(2,3)
         await bot.send_message(chat , "/hunt")



@bot.on(events.NewMessage(outgoing=True,pattern='.go'))
async def begin(event):
    global hunt
    hunt = True
    x = await bot.send_message(chat , "/hunt")
    try:  
     async with bot.conversation('@Hexamonbot') as conv:
       await conv.get_response(x.id)
    except:
       await zzz(2,3)
       await bot.send_message(chat , "/hunt")
    for i in range(1,10000):
      await zzz(randint(1000, 1020))
      await bot.send_message(chat , "/hunt")

@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
    if hunt == True:
     text = event.message.text
     hun = True
     message = await bot.get_messages(chat, ids=event.message.id)
     if ("A shiny" in text):
        bot.disconnect()
     elif("TM" in text):
        print(event.message.text)
        await zzz(randint(2,3))
        x = await bot.send_message(chat , "/hunt")
        try:  
         async with bot.conversation('@Hexamonbot') as conv:
           await conv.get_response(x.id)
        except:
           await zzz(2,3)
           await bot.send_message(chat , "/hunt")
     elif any(item in text for item in list):
        await message.click(text="Battle")
        await message.click(text="Battle")
        await message.click(text="Battle")
     elif("A wild" in text or "An expert" in text):
      if hun == False:
       pass
      else:
       await zzz(randint(2,5))
       x = await bot.send_message(chat , "/hunt")
       try:  
        async with bot.conversation('@Hexamonbot') as conv:
          await conv.get_response(x.id)
       except:
          await zzz(2,3)
          await bot.send_message(chat , "/hunt")
      

@bot.on(events.NewMessage(chats=chat,incoming=True))
async def hunt(event):
   print(event.message.text)
   if event.message.text[:13] == "Battle begins":
        message = await bot.get_messages(chat, ids=event.message.id)
        await zzz(2)
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")
        await message.click(text = "Poke Balls")      


@bot.on(events.MessageEdited(chats=chat))
async def cacther(event):
   message = await bot.get_messages(chat, ids=event.message.id)
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls")
   await message.click(text = "Poke Balls") 
   if event.message.text[:4] == "Wild":
      await zzz(2)
      await message.click(text = "Ultra")
      await message.click(text = "Ultra")
      await message.click(text = "Ultra")
   if any(keyword in event.message.text for keyword in ['fled', 'fainted', 'caught']):
      await zzz(randint(2,5))
      x = await bot.send_message(chat , "/hunt")
      try:  
       async with bot.conversation('@Hexamonbot') as conv:
         await conv.get_response(x.id)
      except:
         await zzz(2,3)
         await bot.send_message(chat , "/hunt")





@bot.on(events.NewMessage(outgoing=True,pattern='.stop'))
async def stop(event):
    global hunt
    hunt = False


bot.start()
bot.run_until_disconnected()