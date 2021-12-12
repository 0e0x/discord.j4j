import discord, time, os, random
from discord.ext import commands
from replit import db

#-------------#
db['dmed'] = []
#-------------#

bot = commands.Bot(
      self_bot = True,
      command_prefix = "j4j"
)
#-------------------------#

j4j_list = [
           'j4j fast',
           'j4j pls',
           'j4jing, no bots',
           'j4j anyone',
           'j4j quickly',
           '> j4j, 20 members',
           '> j4j ',
           '> **j4j** im not a bot'
]

#--------------------------#

token   = ''
invite  = ''

#--------------------------#

@bot.event
async def on_ready():
          print('+== READY AS {} ==+'.format(bot.user.name)
          
          while True:
                for guild in bot.guilds:
                    for channel in guild.channels:
                        if 'j4j' and 'ads' or 'j4j' and 'fast' in channel.name:
                            c = await bot.fetch_channel(channel)
                            await c.send(random.choice(j4j_list))
                        else:
                            pass
                      
#--------------------------------------------------#                    

@bot.event
async def on_message(message):
          if isinstance(message.channel, discord.channel.DMChannel):
                 if message.author.id != bot.user.id:
                    if message.author.id not in db['dmed']:
                       await message.channel.send('**j4j** fast, you first, {}'.format(invite))
                       #-#
                       db['dmed'] += [message.author.id]
                       print(' -- {} dmed you, so responded to the dms'.format(message.author))
                       #-#
                    else:
                       print(' -- {} dmed you '.format(message.author.name))
                       
#----------------------------------------------------#

bot.run(token, bot = False)
