import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import time
import os
import colorsys
import random
import json
 
client = Bot(description="SciBot is best", command_prefix="&", pm_help = False)
dark = discord.Client()
user_id = message.author.id
author_level = get_level(user_id)
author_xp = get_xp(user_id)

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started SciBot')
    print('Created by Utkarsh')
 
 
@dark.event
async def on_message(message):
    user_id = message.author.id

    author_level = get_level(user_id)
    author_xp = get_xp(user_id)

    if author_level == 0 and author_xp >= 100:
        set_level(user_id, 1)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Level Up!')
        embed.add_field(name = 'Congratulations User! ',value ='{}'.format(message.author.name),inline = False)
        embed.add_field(name = 'You are at ',value ='Level 1! Chat more and stay active to rankup fast',inline = False)
        await dark.send_message(channel, embed=embed)

    if author_level == 1 and author_xp >= 200:
        set_level(user_id, 2)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Level Up!')
        embed.add_field(name = 'Congratulations User! ',value ='{}'.format(message.author.name),inline = False)
        embed.add_field(name = 'You are at ',value ='Level 2! Chat more and stay active to rankup fast',inline = False)
        await dark.send_message(channel, embed=embed)
        
    if author_level == 2 and author_xp >= 250:
        set_level(user_id, 3)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Level Up!')
        embed.add_field(name = 'Congratulations User! ',value ='{}'.format(message.author.name),inline = False)
        embed.add_field(name = 'You are at ',value ='Level 3! Chat more and stay active to rankup fast',inline = False)
        await dark.send_message(channel, embed=embed)
    if author_level == 3 and author_xp >= 300:
        set_level(user_id, 4)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Level Up!')
        embed.add_field(name = 'Congratulations User! ',value ='{}'.format(message.author.name),inline = False)
        embed.add_field(name = 'You are at ',value ='Level 4! Chat more and stay active to rankup fast',inline = False)
        await dark.send_message(channel, embed=embed)
    if author_level == 4 and author_xp >= 400:
        set_level(user_id, 5)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Level Up!')
        embed.add_field(name = 'Congratulations User! ',value ='{}'.format(message.author.name),inline = False)
        embed.add_field(name = 'You are at ',value ='Level 5! Chat more and stay active to rankup fast',inline = False)
        await dark.send_message(channel, embed=embed)
    if author_level == 8 and author_xp >= 700:
        set_level(user_id, 9)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Level Up!')
        embed.add_field(name = 'Congratulations User! ',value ='{}'.format(message.author.name),inline = False)
        embed.add_field(name = 'You are at ',value ='Level 9! Chat more and stay active to rankup fast',inline = False)
        await dark.send_message(channel, embed=embed)
    if author_level == 9 and author_xp >= 1000:
        set_level(user_id, 10)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Level Up!')
        embed.add_field(name = 'Congratulations User! ',value ='{}'.format(message.author.name),inline = False)
        embed.add_field(name = 'You are at ',value ='Level 10! Chat more and stay active to rankup fast',inline = False)
        await dark.send_message(channel, embed=embed)

    if message.content.lower().startswith('mv!xp'):
        await dark.send_message(message.channel, "You have `{}` XP!".format(get_xp(message.author.id)))

    if message.content.lower().startswith('mv!lvl'):
        level = get_level(user_id)
        await dark.send_message(message.channel, "You are at Level: {}".format(level))

    user_add_xp(message.author.id, 2)


def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("users.json"):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['xp'] += xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['xp'] = xp
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['xp']
    else:
        return 0


def set_level(user_id: int, level: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        users[user_id]["level"] = level
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_level(user_id: int):
    if os.path.isfile('users.json'):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            return users[user_id]['level']
        except KeyError:
            return 0   
 
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
    if message.author.bot:
      return
    if message.channel.name == '╰☆☆-multiverse-log-☆☆╮':
     return
    else:
      user = message.author
      for channel in user.server.channels:
        if channel.name == '╰☆☆-multiverse-log-☆☆╮':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_author(name='Message deleted')
            embed.add_field(name = 'User: **{0}**'.format(user.name),value ='UserID: **{}**'.format(user.id),inline = False)
            embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
            embed.add_field(name = 'Channel:',value ='{}'.format(message.channel.name),inline = False)
            await client.send_message(channel, embed=embed)
 
@client.event
async def on_message(message):
    user = message.author
    if message.author.bot:
      return
    else:
      if message.content.startswith('mv!donate'):
          msg = '**Support us by donating us;** https://www.paypal.me/RVerma181'
          await client.send_message(message.channel, msg)
        
      if 'Who is your creator bot?' in message.content:
          msg = 'DarkLegend#3807 is my creator'.format(message)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'hi bot' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'hello bot' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'Hi bot' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
          
      if 'Hello bot' in message.content:
          msg = 'Hello {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
          
      if 'how are you bot?' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'How are you bot?' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
          
      if 'sup bot' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)
         
      if 'Sup bot' in message.content:
          msg = 'I am fine what about you? {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)         
          
      if 'I am also fine bot' in message.content:
          msg = 'Cool! {}'.format(message.author.name)
          msg2 = await client.send_message(message.channel, msg)          
         
      if 'i am also fine bot' in message.content:
          msg = 'Cool! {}'.format(message.author.name)
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
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
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
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
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
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
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
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
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
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
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
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
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
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
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
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
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
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
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
                embed.add_field(name = 'Message:',value ='{}'.format(message.content),inline = False)
                await client.send_message(channel, embed=embed)
        
client.run(os.getenv('Token'))
