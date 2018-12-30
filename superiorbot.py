import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'A New Wild Member Appeared')
    print('Sent message to ' + member.name)
    await client.change_presence(game=Game(name='Playing Camshitstudio'))
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hello,I Hope You Will like Our Server')
    print('Sent message to ' + member.name)
    await client.change_presence(game=Game(name='Playing Fortnite'))
    await client.change_presence(game=Game(name='fortnite'))
    print('Ready') 


@client.event
async def on_message(message):
    if ('heck') in message.content:
       await client.delete_message(message)
    if ('fuck') in message.content:
       await client.delete_message(message)
    if ('bitch') in message.content:
       await client.delete_message(message)
    if ('tf') in message.content:
       await client.delete_message(message)
    if message.content == 'Dbz':
        em = discord.Embed(description='SuperiorRup!!!!')
        em.set_image(url='https://ibb.co/zn3RZJk')
        await client.send_message(message.channel, embed=em)
    if message.content == 'ping':
        await client.send_message(message.channel,'pong')
    if message.content == 'hey':
        await client.send_message(message.channel,'hello')
    if message.content == 'yo':
        await client.send_message(message.channel,'yo')
    if message.content == 'watsup':
        await client.send_message(message.channel,'sky')
    if message.content == 'who is your master':
        await client.send_message(message.channel,'SuperiorRup')
    if message.content.startswith('+facts'):
        randomlist = [do you know rup loves nfs payback but he used to play fortnite]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior Rup's real hair color is black]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior makes videos with Camtasia 9]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior dont like naps,he like sleeping]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior is very lazy]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior is my master]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior most favorite food is pizza]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior most favorite food is burger]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior favorite colour is blue]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior is working on new video]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior is very Rude from opposite side]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior loves Games]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Superior best friend is Zakktur Gamer]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Zakktur gamer is very smart]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Zakktur gamer manages everything]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [Zakktur gamer is sometimes rude but he is nice]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+facts'):
        randomlist = [I was Created by The Help of Superior Rup and Zakktur Gamer]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '!help':
        await client.send_message(message.channel,'please checkout #commands ')
    if message.content == '!i am new':
        await client.send_message(message.channel,'hope you will like our server,have a good day')
    if message.content == '!hi':
        await client.send_message(message.channel,'Hello,Have a Good Day')
    if message.content == 'Sub4sub':
        await client.send_message(message.channel,'we will mute you if u do that again')
    if message.content == '!i love you':
        await client.send_message(message.channel,'awww.......You are so cute')
    if message.content.startswith('!watsup'):
        randomlist = [Sky]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!watsup'):
        randomlist = [kite]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!watsup'):
        randomlist = [Superior Rup's channel]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!watsup'):
        randomlist = [nothing]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!watsup'):
        randomlist = [good,wat about you]
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run('NTI4NTA0MzMyMjYyMzA5ODg4.DwoD7A.ckYWri-lEriTcHNAsupTOxD5a94')
