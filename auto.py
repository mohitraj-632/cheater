import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType

client = Bot(command_prefix="+", pm_help = True)
client.remove_command('help')

channel = client.get_channel("738698939162951751")
	
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Direct Message BOT')
    print('Created by low')
    client.loop.create_task(status_task())
 
	
def is_owner(ctx):
    return ctx.message.author.id == "662505445566709781","505756286336368652"

@client.command(pass_context = True)
@commands.check(is_owner)
async def restart():
    await client.logout()

@client.event
async def on_message(message):
	await client.process_commands(message)

@client.command(pass_context=True)
async def add(ctx,num:int):
        await client.send_message(channel,f".add {num}")

@client.command(pass_context=True)
async def code(ctx,code:int):
        await client.send_message(channel,f".code {code}")

client.run('NzM5MTM3NDA5MTk0NjU1NzQ1.XyWF9w.SeZ86JGvpdgyL3SlaJe_99klo2E', bot=False)
