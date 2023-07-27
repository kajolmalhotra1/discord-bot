import discord   #import discord module

client = discord.Client(intents=discord.Intents.default())     #client initialize

@client.event   #event listen
async def on_ready():   #creating function on_ready()
 print("Bot is currently ready!")

@client.event
async def on_message(message):
  if message.author == client.user:
   return

  if message.content.lower() == "!hello":
   await message.channel.send("Greetings!")

  elif message.content.lower() == "name":
   embed = discord.Embed(title="Hi I am neobot!", description="Nice to meet you", color=0x00ff00)
  await message.channel.send(embed=embed)

token = "MTEzNDA3NjIyMDc0MTUyOTYyMA.GjoK7z.UpGROSt2WKZCK3HU44e2bQPOE74xE5X-psP4GU"

if __name__ == '__main__':    # for running token
    client.run(token)