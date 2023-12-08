import os
import discord
from discord.ext import commands

from server import server
 



intents = discord.Intents.default()
intents.members = True





#--------------------------------------------------------------------------------------------------------
#PREFIX
bot = commands.Bot(command_prefix="u!",
intents = discord.Intents.all())
#----------------------------------------------------------------------------------------------------------

#status !! 
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"
  ))
#--------------------------------------------------------------------------------------------------------------------
#TRIGGERED COMMANDS


@bot.command()
async def hello(ctx):
    await ctx.send("Hi!!")


@bot.command()
async def bye(ctx):
    await ctx.send("See ya!!")

#----------------------------------------------------------------------------------------

#The reality..........

'''@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.message.add_reaction("reaction")

    await ctx.send(f"{member.name} has been kicked by {ctx.author.name}!")
    await log_channel.send(f"{ctx.author.name} has kicked {member.display_name}")'''


#--- kick command --- 
@bot.command() 
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user} Has been kicked!")

@kick.error 
async def kick(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("Oops, You're not doing this!!")

#--- ban command --- 
@bot.command() 
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} Has been banned!")

@ban.error 
async def ban(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("Oops, You're not doing this!!")

#--- unban command --- 
@bot.command() 
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int):
  user_id = await bot.fetch_user(id)
  await ctx.guild.unban(user_id)
  await ctx.send(f"{user_id} Has been unbanned!")

@unban.error
async def ban(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("Oops, You're not doing this!!")

#-------------------------------------------------------------------------------------------------------------

#--- Purge message delete ---

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, limit):
    await ctx.message.delete()
    limit = int(limit)
    deleted = await ctx.channel.purge(limit=limit)
    cofirmdelete_embed = discord.Embed(title='yeyyy, you deleted a lot...', description=f'Deleted {len(deleted)} messages in #{ctx.channel}', color=0x4fff4d)
    await ctx.channel.send(embed=cofirmdelete_embed, delete_after=4.0)

  
#-------------------------------------------------------------------------------------------------------------
#LAST PLACE!!

server()
TOKEN = os.environ['TOKEN']
bot.run(TOKEN)
