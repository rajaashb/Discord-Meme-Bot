import discord
import requests
import json
from dotenv import load_dotenv
import os
from keep_alive import keep_alive

keep_alive()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

def get_meme():
    response = requests.get('https://meme-api.com/gimme')  #make http request to get meme data from reddit
    json_data = json.loads(response.text)  #read json data
    return json_data['url']  #return the image's url

class MyClient(discord.Client):
    async def on_ready(self):  #on_ready() function will be called when the Discord bot's login is successful
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):  #on_message() method gets called automatically anytime there is a new message in a channel where bot is located
        if message.author == self.user:  #checking  if the bot is the one sending the message in the chat
            return

        if message.content.startswith('$meme'):  #respond to a special keyword $meme
            await message.channel.send(get_meme())

intents = discord.Intents.default()  #settings for what Discord bot can access
intents.message_content = True  #explicitly allow it to interact with messages

client = MyClient(intents = intents)
client.run(TOKEN)
