import discord

client = discord.Client()

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


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

client.run('MzI2ODQ3NTcyNjIwNjA3NDg5.DCt68Q.AU-rTgTqXR5hEav56yXvrkjSM2k')
