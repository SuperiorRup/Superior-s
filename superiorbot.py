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
client.run('NTI4NTA0MzMyMjYyMzA5ODg4.DwjdtQ.u4FCOBy47ISfeE61-fnRjJVV1AQ')
