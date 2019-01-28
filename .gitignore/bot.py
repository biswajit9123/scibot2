import discord
import asyncio
from discord.ext.commands import Bot
import platform
import time
import os
from google.cloud import translate
import colorsys
import random
import json
 
client = Bot(description="MyBot is best", command_prefix="mv!", pm_help = False)
client.remove_command('help')

keyfile = open("keys.txt", "r")
key = keyfile.read(60)

global last_message
last_message = "This is a placeholder"

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started SciBot')
    print('Created by Utkarsh')
 
@client.event 
async def on_member_join(member):
    if member.bot:
      return
    if member.server.id == "404622530129690624":
      print("In our server" + member.name + " just joined")
      nickname = '[GGC]' + member.name
      await client.change_nickname(member, nickname)
    if member.server.id == "488267422449664011":
      nickname = 'AGC|' + member.name
      await client.change_nickname(member, nickname)
    if member.server.id == "527430758902661121":
      role = discord.utils.get(member.server.roles, name='Guest')
      await client.add_roles(member, role)
      await client.send_message(member, f'Hey {member.name}, Check <#527481608530558980> for more information about our giveaways')
    if member.server.id == "534158752597671956":
      embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Hope you will enjoy our content. Do not forget to check rules and never try to break any one of them.', color = 0x36393E)
      embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
      embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
      embed.set_image(url = 'https://cdn.pbrd.co/images/HXJvPMP.gif')
      embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
      embed.add_field(name='Time of joining', value=member.joined_at)
      await client.send_message(member, embed=embed) 
      
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
    global last_message
    content = message.content
    user = message.author
    if message.author.bot:
      return
    if message.server.id == '264445053596991498':
      return
    if message.content.startswith('mv!say'):
      return
    else:
      if content.startswith("mv!translate"):
        if " " in content:
          # When the user wants to call for help, or translate to more than english, this will parse their intention
          args = content.split(" ", 1)[1]
          langcode = check_language(args,'language')
          if args.lower() == "help":
            help_message = "Type **.translate** to translate the message above to english.\n" \
                           " Type **.translate <language>** to translate it to that language."
            await client.send_message(message.channel, help_message)
          elif langcode != "False":
            translation = translate_message(last_message, langcode)
            formatted_return = format_response(translation)
            await discord_client.send_message(message.channel, formatted_return)
          else:
            translation = translate_message(last_message, "en")
            formatted_return = format_response(translation)
            await client.send_message(message.channel, formatted_return)
            last_message = content
      if message.content.startswith('mv!donate'):
          msg = '**Support us by donating us on PayPal:** https://www.paypal.me/RVerma181\n**Support us by donating us on Patreon:** https://www.patreon.com/multiverseofficial'
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
         
      if message.content.startswith('<@515403515217313795>') and message.content.endswith('<@515403515217313795>'):
          msg = 'Hey {}, use ``mv!help`` or <@515403515217313795>`` help`` to get all commands list in dm'.format(message.author.name)
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


def translate_message(message, target):
    translate_client = translate.Client.from_service_account_json('api-key.json')
    result = translate_client.translate(message, target_language=target)
    return result


# Takes in a string that may or may not be a language code.
# If it is a language code, it returns said code.
# If it is a language, it returns the affiliated code. If not, it returns -1
def check_language(code, target):
    with open('languages.json') as data:
        languages = json.load(data)
        for lang in languages:
            if (lang['language'].lower() == code.lower())or (lang['name'].lower() == code.lower()):
                return lang[target]
        return "False"


def format_response(response):
    language_code = response['detectedSourceLanguage']
    language_name = check_language(language_code, 'name')
    formatted_return = ("```" + "\n" + " \"" + response['translatedText'] + "\"\n" + "```" + "\n" +
                        "**Source Language:** " + language_name + " **|** " + language_code + "\n")
    return formatted_return
        
client.run(os.getenv('Token'))
