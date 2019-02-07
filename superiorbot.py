import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '+')
Clientdiscord = discord.Client()

client.remove command('+help')

@client.event
async def on_member_join():
    print('Ready')
    print ("Starting up")
    await client.change_presence(game=discord.Game(name=";help", type=1))
    print ("My username is " + client.user.name + " and i am running with the ID: " + client.user.id)
    await client.change_presence(game=discord.Game(name="Superior Videos", type=2))
    print ("status2")
    await client.change_presence(game=discord.Game(name="+Help", type=3))
    print ("status3")
    await client.change_presence(game=discord.Game(name="In 1 Server", type=4))
    print ("Started")
    await client.change_presence(game=discord.Game(name="Fortnite", type=3))

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
     
    if message.content == 'hey':
        await client.send_message(message.channel,'hello')
    if message.content == 'Yo':
        await client.send_message(message.channel,'hi')
    if message.author == client.user:
        return

    if message.content.startswith('+ping'):
        msg = 'Pong!{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        

    if message.content == 'watsup':
        await client.send_message(message.channel,'sky')
    if message.content == 'who is your master':
        await client.send_message(message.channel,'SuperiorRup')
    if message.content.startswith('+flipcoin'):
        randomlist = ['Head','tail']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('+what should i play'):
        randomlist = ['fortnite','cs:go','pubg','nothing']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '+fact1':
        await client.send_message(message.channel,'Rup real hair colour is black')
    if message.content == '+fact2':
        await client.send_message(message.channel,'Rup is very Lazy')
    if message.content == '+fact3':
        await client.send_message(message.channel,'Rup favorite food is Fast food')
    if message.content == '+fact4':
        await client.send_message(message.channel,'Rup loves pizza')
    if message.content == '+fact5':
        await client.send_message(message.channel,'Rup is working on new video')
    if message.content == '+what rup is doing':
        await client.send_message(message.channel,'Creating new videos for you guys')
    if message.content == 'SUBS4SUBS':
        em = discord.Embed(description='')
        em.set_image(url='')
        await client.send_message(message.channel, embed=em)
    if ('SUBS4SUBS') in message.content:
       await client.delete_message(message)
    if ('Subs4subs') in message.content:
       await client.delete_message(message)
    if ('subs4subs') in message.content:
       await client.delete_message(message)
    if ('dumbass') in message.content:
        await client.delete_message(message)
        @client.command(pass_context=True)
async def Zeon(ctx):
    await client.say("Yes!")
    print ("reply Posted")
@client.command(pass_context = True)
async def ping(ctx):
        embed=discord.Embed(title="**PONG!**", description="Command Accepted!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    return await client.say(mesg)
@client.command(pass_context = True)
async def adminhelp(ctx):
        embed=discord.Embed(title="**ADMIN COMMANDS**", description="**purge <1-100>**\n**botinfo**\n**ban**\n**clearwarn**\n**warn**\n**kick**\n**mute**\n**unmute**\n**coming soon...**".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def invite(ctx):
        embed=discord.Embed(title="**Our Server Link**", description="https://discord.gg/CrMKHMb".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context=True)
async def totalmembers(ctx):
        embed=discord.Embed(title="**TOTAL MEMBERS OF {0.name}**", description="MEMBERS- {0.member_count}".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def mexayt(ctx):
        embed=discord.Embed(title="**HERE IS THE LINK OF SUPERIOR RUP CHANNEL**", description="https://www.youtube.com/channel/UCguNIP794svRhgGTAWE7JDg?view_as=subscriber".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def zeonlink(ctx):
        embed=discord.Embed(title="**HERE IS THE LINK OF ZEON**", description="https://discordapp.com/oauth2/authorize?client_id=542649204141457409&scope=bot&permissions=2146958591".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed) 
@client.command(pass_context = True)
async def help(ctx):
        embed=discord.Embed(title="**NORMAL COMMANDS**", description="**join**\n**zeonlink**\n**adminhelp**\n**say**\n**botinfo**\n**ping**\n**invite**\n**join - coming soon...**\n****".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def botinfo(ctx):
        embed=discord.Embed(title="**INFORMATIONS OF Zeon**", description="**Name-ZEON**\n**Creator- Superior Rup**\n**Official Server- ZEON**\n**Bot Type- Public**\n**Discord.py**".format(member, ctx.message.author), color=0x7289da)
        await client.say(embed=embed)
        print ("helped")        
@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        await client.kick(userName)
        embed=discord.Embed(title="**User Kicked Successfully!**", description="**The User was successfully Kicked!**".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="**User unmuted!**", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def purge(ctx, number):
 if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
    mgs = [] 
    number = int(number) 
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="**User muted!**", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def clearwarn(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="**Warning Cleared!!**", description="Warning of **{0}** was cleared by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)   
@client.command(pass_context = True)
async def warn(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="**User Warned!**", description="**{0}** was warned **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def ban(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        await client.ban(userName)
        embed=discord.Embed(title="**User Banned Successfully!**", description="**The User was successfully Banned!**".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
@client.command(pass_context = True)
async def unban(ctx, userName: discord.User):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '519122918773620747':
        await client.unban(userName)
        embed=discord.Embed(title="**User Banned Successfully!**", description="**The User was successfully Banned!**".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title="Command not accepted!", description="Sorry! You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
        
client.run('NTQyOTE4ODY4NTI0MzM1MTE2.Dz1ArA.FCNR0hO3IMTl_pA9x99IjCGCIEE')
