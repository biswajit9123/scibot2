import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import time
import os
 
client = Bot(description="SciBot is best", command_prefix="&", pm_help = False)

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}! Please check rules and never try to break any rules.'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_member_leave(member):
    server = member.server
    fmt = '{0.mention} just left {1.name}!'
    await client.send_message(server, fmt.format(member, server))
    
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started SciBot')
    print('Created by Utkarsh')
    return await client.change_presence(game=discord.Game(name='Reasearching More on Science&Tech | Looking for &help'))
 
    if message.content.startswith('gm'):
        msg = 'Good Morining! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
@client.event
async def on_message(message):
    if 'Who is your creator?' in message.content:
        msg = 'DarkLegend#3807 is my creator'.format(message)
        msg2 = await client.send_message(message.channel, msg)
       
    if 'fuck' in message.content:
        msg = 'Do not use bad words {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg2)
        
    if 'FUCK' in message.content:
        msg = 'Do not use bad words {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg2)
        
    if 'asshole' in message.content:
        msg = 'Do not use bad words {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg2)
        
        
    if 'ASSHOLE' in message.content:
        msg = 'Do not use bad words {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg2)
        
        
    if 'Bahench' in message.content:
        msg = 'Do not use bad words {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg2)
        
    if 'Fuck' in message.content:
        msg = 'Do not use bad words {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg2)
        
    if 'chut' in message.content:
        msg = 'Do not use bad words {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg2)
        
        
    if 'chod' in message.content:
        msg = 'Do not use bad words {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg2)
        
    if 'Chod' in message.content:
        msg = 'Do not use bad words {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg2)
       
    if 'bsdk' in message.content:
        msg = 'Do not use bad words {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg2)
       
    if 'bhosd' in message.content:
        msg = 'Do not use bad words {0.author.name}'.format(message)
        msg2 = await client.send_message(message.channel, msg)
        await client.delete_message(message)
        await asyncio.sleep(5)
        await client.delete_message(msg2)
        
client.run(os.getenv('Token'))
