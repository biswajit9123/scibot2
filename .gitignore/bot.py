import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import time
import os
import colorsys
import random
 
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
async def on_message_delete(message):
    user = message.author
    for channel in user.server.channels:
      if channel.name == '╰☆☆-multiverse-log-☆☆╮':
          r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
          embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
          embed.set_author(name='Message deleted')
          embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
          embed.add_field(name = 'Message:',value ='{}'.format(message.name),inline = False)
          embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
          await client.send_message(channel, embed=embed)
 
@client.event
async def on_message(message):
    user = message.author
    if message.author.bot:
      return
    else:
      if 'Who is your creator?' in message.content:
          msg = 'DarkLegend#3807 is my creator'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          
      if 'fuck' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-multiverse-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **fuck**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
      
      if 'FUCK' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-multiverse-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **FUCK**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
        
      if 'asshole' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-multiverse-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **asshole**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
        
      if 'ASSHOLE' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-multiverse-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **ASSHOLE**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
                
      if 'Fuck' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-multiverse-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Fuck**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='English bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
        
      if 'chut' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-multiverse-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **chut**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
        
      if 'chod' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-multiverse-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **chod**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
        
      if 'Chod' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-multiverse-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **Chod**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
       
      if 'bsdk' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-multiverse-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **bsdk**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word(Shortform abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
       
      if 'bhosd' in message.content:
          msg = 'Do not use bad words {0.author.name}'.format(message)
          msg2 = await client.send_message(message.channel, msg)
          await client.delete_message(message)
          await asyncio.sleep(5)
          await client.delete_message(msg2)
          for channel in user.server.channels:
            if channel.name == '╰☆☆-multiverse-log-☆☆╮':
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name='Warned user')
                embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
                embed.add_field(name = 'Reason: **Used bad words**',value ='Word: **bhosd...**',inline = False)
                embed.add_field(name = 'Type of bad word:',value ='Hindi bad word(Short form abuse)',inline = False)
                embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
                await client.send_message(channel, embed=embed)
        
client.run(os.getenv('Token'))
