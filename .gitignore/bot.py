import discord
import asyncio
from discord.ext.commands import Bot
import platform
import time
import os
import colorsys
import random
import json
 
client = Bot(description="MyBot is best", command_prefix="mv!", pm_help = False)
client.remove_command('help')


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started SciBot')
    print('Created by Utkarsh')
 
@client.event
async def on_member_join(member):
    if member.server.id == "404622530129690624":
     print("In our server" + member.name + " just joined")
     nickname = '[GGC]' + member.name
     await client.change_nickname(member, nickname)

 
@client.event
async def on_message_edit(before, after):
    if before.content == after.content:
      return
    if before.author == client.user:
      return
    else:
      user = before.author
      member = after.author
      for channel in user.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_author(name='Message edited')
            embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
            embed.add_field(name = 'Before:',value ='{}'.format(before.content),inline = False)
            embed.add_field(name = 'After:',value ='{}'.format(after.content),inline = False)
            embed.add_field(name = 'Channel:',value ='{}'.format(before.channel.name),inline = False)
            await client.send_message(channel, embed=embed)
 
@client.event
async def on_message_delete(message):
    if not message.author.bot:
      channelname = '╰☆☆-multiverse-log-☆☆╮'
      logchannel=None
      for channel in message.server.channels:
        if channel.name == channelname:
          user = message.author
      for channel in user.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
          logchannel = channel
          r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
          embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
          embed.set_author(name='Message deleted')
          embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
          embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
          embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
          await client.send_message(logchannel,  embed=embed)
          
          
@client.event
async def on_reaction_add(reaction, user):
  for channel in user.server.channels:
    if channel.name == '╰☆☆-multiverse-log-☆☆╮':
        logchannel = channel
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Reaction Added')
        embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
        embed.add_field(name = 'Message:',value ='{}'.format(reaction.message.content),inline = False)
        embed.add_field(name = 'Channel:',value ='{}'.format(reaction.message.channel.name),inline = False)
        embed.add_field(name = 'Emoji:',value ='{}'.format(reaction.emoji),inline = False)
        await client.send_message(logchannel,  embed=embed)
        
@client.event
async def on_reaction_remove(reaction, user):
  for channel in user.server.channels:
    if channel.name == '╰☆☆-multiverse-log-☆☆╮':
        logchannel = channel
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Reaction Removed')
        embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
        embed.add_field(name = 'Message:',value ='{}'.format(reaction.message.content),inline = False)
        embed.add_field(name = 'Channel:',value ='{}'.format(reaction.message.channel.name),inline = False)
        embed.add_field(name = 'Emoji:',value ='{}'.format(reaction.emoji),inline = False)
        await client.send_message(logchannel,  embed=embed)
 
 
@client.event
async def on_message(message):
    user = message.author
    if message.author.bot:
      return
    if message.server.id == '264445053596991498':
      return
    if message.content.startswith('mv!say'):
      return
    else:
      if message.content.startswith('mv!donate'):
          msg = '**Support us by donating us;** https://www.paypal.me/RVerma181'
          await client.send_message(message.channel, msg)
          
      if 'Who is your creator <@515403515217313795>?' in message.content:
          msg = 'DarkLegend#3807 is my creator'.format(message)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'hi <@515403515217313795>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'bye <@515403515217313795>' in message.content:
          msg = 'Bye {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)

      if 'good night <@515403515217313795>' in message.content:
          msg = 'Good night {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)

      if 'Good night <@515403515217313795>' in message.content:
          msg = 'Goodd night {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'Good morning <@515403515217313795>' in message.content:
          msg = 'Good Morning {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)

      if 'good morning <@515403515217313795>' in message.content:
          msg = 'Good Morning {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'Good afternoon <@515403515217313795>' in message.content:
          msg = 'Good afternoon {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'good afternoon <@515403515217313795>' in message.content:
          msg = 'Good afternoon {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'Bye <@515403515217313795>' in message.content:
          msg = 'Bye {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
                 
      if 'hello <@515403515217313795>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'Hi <@515403515217313795>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
          
      if 'Hello <@515403515217313795>' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
          
      if 'how are you <@515403515217313795>?' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'How are you <@515403515217313795>?' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
          
      if 'sup <@515403515217313795>' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'Sup <@515403515217313795>' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)         
          
      if 'I am also fine <@515403515217313795>' in message.content:
          msg = 'Cool! {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)          
         
      if 'i am also fine <@515403515217313795>' in message.content:
          msg = 'Cool! {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)          

        
client.run(os.getenv('Token'))
