import discord
from discord.ext import commands
import youtube_dl
from random import randint

description = '''Jarvis bot. '''

client = discord.Client()
bot = commands.Bot(command_prefix='!', description=description)

#Function to handle on_message event
@client.event
async def on_message(message):
    #Per the discord.py docs this is to not have the bot respond to itself
    if message.author == client.user:
        return
    
    #If the bot sees the command !hello we will respond with our msg string
    if message.content.startswith('!hello'):
        msg = 'Hello, Master {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
    #If the bot sees the command !Thomas we will respond with our msg string
    if message.content.startswith('!Thomas') | message.content.startswith('!thomas'):
        msg = 'Thomas is indeed a deadbeat paraplegic'.format(message)
        await client.send_message(message.channel, msg, tts=True)

    await bot.process_commands(message)

#Command that makes bot play requested youtube song
@bot.command(pass_context = True)
async def play(ctx):
    message = ctx.message
    channel = ctx.message.channel
    author = ctx.message.author
    voice_channel = author.voice_channel
    for i in client.voice_clients:
        if (i.server == ctx.message.server):
            msg = "Master {0.author.mention}, I am already in the channel.".format(message)
            return await client.send_message(channel, msg)
    url = await client.parsemessage(message)
    vc = await client.join_voice_channel(voice_channel)
    player = await vc.create_ytdl_player(url)
    player.start()
    player.volume = 0.1

#Makes bot leave voice channel
@bot.command(pass_context = True)
async def stop(ctx):
    message = ctx.message
    channel = ctx.message.channel
    for i in client.voice_clients:
        if(i.server == ctx.message.server):
            return await i.disconnect()
    msg = "Master {0.author.mention}, I am not currently in the voice channel.".format(message)
    return await client.send_message(channel, msg)

#Command to make bot display when a specific member joined
@bot.command(pass_context = True)
async def joined(ctx, member : discord.Member = None):
    """Says when a member joined."""
    message = ctx.message
    channel = ctx.message.channel
    if(member != None):
        await client.send_message(channel, '{0.name} joined in {0.joined_at}'.format(member))
    else:
        msg = 'Master {0.author.mention}, you forgot to mention a member of the server.'.format(message)
        await client.send_message(channel, msg)

#Makes bot parse string based on " " character
@client.event
async def parsemessage(message):
    m_content = message.content
    message_list = m_content.split()
    if (len(message_list) != 2):
        error_message = "Sorry master {0.author.mention}, this command takes one argument.".format(message)
        return error_message
    return message_list[1]

#Function used for deciding what game to play within the channel (BETA Usage)
@bot.command(pass_context = True)
async def game(ctx):
    message = ctx.message
    channel = ctx.message.channel
    game = randint(0, 4)
    if game == 0:
        msg = 'I would suggest League of Legends.'.format(message)
        await client.send_message(channel, msg)
    if game == 1:
        msg = 'I would suggest Rainbow Six Siege.'.format(message)
        await client.send_message(channel, msg)
    if game == 2:
        msg = 'I would suggest Black Desert.'.format(message)
        await client.send_message(channel, msg)
    if game == 3:
        msg = 'I would suggest PUBG.'.format(message)
        await client.send_message(channel, msg)
    if game == 4:
        msg = 'I would suggest Payday 2, even though it is a deplorable game.'.format(message)
        await client.send_message(channel, msg)

#No clue wtf this does
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run('MzI2ODQ3NTcyNjIwNjA3NDg5.DCt68Q.AU-rTgTqXR5hEav56yXvrkjSM2k')
