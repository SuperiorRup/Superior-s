import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import member
from discord.utils import get
import asyncio
import random

commandprefix = "+"
client = commands.Bot(command_prefix=commandprefix)
client.remove_command('help')
async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name="PUBG"))
        await asyncio.sleep(10)
        await client.change_presence(game=discord.Game(name="Fortnite with Members"))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name="GTA-V"))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name="Superior's Videos"))
        await asyncio.sleep(15)
        await client.change_presence(game=discord.Game(name="+Help"))
        await asyncio.sleep(3)
        await client.change_presence(game=discord.Game(name="for server"))
        await asyncio.sleep(3)
    
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
async def zeonyt(ctx):
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


