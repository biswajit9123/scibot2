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
 
    if message.content.startswith('hi bot'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)        
    if message.content.startswith('gm'):
        msg = 'Good Morining! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
       
    if message.content.startswith('cya bot'):
        msg = 'Cya! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
       
    if message.content.startswith('bye bot'):
        msg = 'Bye! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
       
    if message.content.startswith('gtg bot'):
        msg = 'gtg! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
       
    if message.content.startswith('yo bot'):
        msg = 'yo {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('Why Ganga river is pure?'):
        msg = '{0.author.mention} Bacteriophage is the bacteria which is the major cause if it. For more information check- https://en.wikipedia.org/wiki/Bacteriophage '.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('What is matter?'):
        msg = '{0.author.mention} Matter maybe defined as-Anything which occupies space,have mass,offers ressistance and can be felt from one or more sence organs. For more information check- https://en.wikipedia.org/wiki/Matter'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('I am also fine'):
        msg = 'Nice :) {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('&spacenews'):
        msg = '**Visit this for todays space news- https://www.sciencealert.com/space** '.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('gn'):
        msg = '**Good Night!** {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('kya haal hai bot'):
        msg = 'Mai thik hu! aur tum {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('mai bhi thik hu'):
        msg = 'Badhiya! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('what a lovely bot'):
        msg = 'Thanks :heart_eyes: ! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('nice bot'):
        msg = 'Thanks :heart_eyes: ! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('What a nice bot'):
        msg = 'Thanks :heart_eyes: ! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
       
    if message.content.startswith('&authlink'):
        msg = 'Authorise this bot using this link- https://discordapp.com/api/oauth2/authorize?client_id=433138197376139277&permissions=8&scope=bot {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('Good Morning'):
        msg = 'Good Morning ! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('Good Night'):
        msg = 'Good Night ! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('&technews'):
        msg = '**Visit this for todays tech news- https://www.sciencealert.com/tech**'.format(message)
        await client.send_message(message.channel, msg)
   
    if message.content.startswith('What are Quarks?'):
        msg = '**Number of subatomic particles carrying a fractional electric charge, knows as building blocks of the hadrons. Quarks have not been directly observed but theoretical predictions based on their existence have been confirmed experimentally. There are 6 types of quarks- 1)Top quark, 2)Bottom Quark, 3)Charm Quark, 4)Up quark, 5)Down Quark and 6)Strange Quark.** *For more info check-* https://en.wikipedia.org/wiki/Quark .'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('i am coding my bot'):
        msg = 'Yeah he is coding me bro! Dont disturb him!'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('&trendgames'):
        msg = '1)PUBG, 2) GTA5 Game, 3)Mini Miltia Tutorials, 4)PUBG Good Edited Videos, etc...'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('&dev'):
        msg = 'This bot is under development.'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('&phynews'):
        msg = '**Visit this for todays physics news- https://www.sciencealert.com/physics**'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('How are you bot?'):
        msg = 'I am fine ! What about you? ! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('sup bot'):
        msg = 'I am fine ! What about you? ! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('chup'):
        msg = 'Talk Properly! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('hatt'):
        msg = 'Talk properly! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('What is streptomycin?'):
        msg = 'An antibiotic that was the first drug to be successful against tuberculosis but is now chiefly used with other drugs because of its toxic side effects.{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
     
    if message.content.startswith('Who is Royal?'):
        msg = 'He is a pro hacker.{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
    if message.content.startswith('Who is your creator bot?'):
        msg = '<@420525168381657090> is my creator.{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
 
       
       
client.run(os.getenv('Token'))
