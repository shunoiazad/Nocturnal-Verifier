import discord
from discord.ext import commands
import os
import asyncio

from keep_alive import keep_alive

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="+", intents=intents)

bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    


@bot.command()
async def verify(ctx):
    role = discord.utils.find(lambda r: r.id == 846546956380798987, ctx.guild.roles)
    
    line = "discord.gg/xs26cbwfpg"
    
    status = ctx.author.status
    activity = ctx.author.activity

    sent = await ctx.reply(embed=discord.Embed(
        title = "Verifying",
        color = discord.Color.gold()
    ))
    
    await asyncio.sleep(1)

    if not role in ctx.author.roles:
        if status.name in ["invisible"]:
            await sent.edit(embed = discord.Embed(
                title = "Verification failed",
                description = "Click [here](https://discord.com/channels/819194655999524914/819449770560585760/847514141995696158) to learn more",
                color = discord.Color.red()
            ))
            
        else:
            if activity:
                if line in activity.name.lower():
                    await ctx.author.add_roles(role)
                    await sent.edit(embed=discord.Embed(
                        title = "You are now verified",
                        color = discord.Color.green()
                    ))
                
                else:
                    await sent.edit(embed = discord.Embed(
                title = "Verification failed",
                description = "Click [here](https://discord.com/channels/819194655999524914/819449770560585760/847514141995696158) to learn more",
                color = discord.Color.red()
            ))
                    
            
            else:
                await sent.edit(embed = discord.Embed(
                title = "Verification failed",
                description = "Click [here](https://discord.com/channels/819194655999524914/819449770560585760/847514141995696158) to learn more",
                color = discord.Color.red()
            ))
                   
                
    else:
        await sent.edit(embed=discord.Embed(
            title = "You are already verified",
            color = discord.Color.red()
        ))
    
    
@bot.command()
@commands.has_permissions(administrator=True)
async def check(ctx):
    role = discord.utils.find(lambda r: r.id == 846546956380798987, ctx.guild.roles)
    line = "discord.gg/xs26cbwfpg"
    
    sent = await ctx.reply(embed=discord.Embed(
        title = "Checking",
        color = discord.Color.gold()
    ))

    await asyncio.sleep(1)

    unroled_members = []

    for user in ctx.guild.members:
        if role in user.roles:
            if user.status.name in ["invisible"]:
                unroled_members.append(f"{user.name}#{user.discriminator}")
                await user.remove_roles(role)
            
            else:
                if user.activity:
                    if not line in user.activity.name.lower():
                        unroled_members.append(f"{user.name}#{user.discriminator}")
                        await user.remove_roles(role)
                    
                else:
                    unroled_members.append(f"{user.name}#{user.discriminator}")
                    await user.remove_roles(role)


    if unroled_members:
        embed = discord.Embed(
            title = "The following users lost their role:",
            description = "\n".join(unroled_members),
            color = discord.Color.red()
        )
        await sent.edit(embed=embed)
        await ctx.send(embed=discord.Embed(
            title = "All good",
             color = discord.Color.green()
        ))
          
    else:     
        await sent.edit(embed=discord.Embed(
            title = "All good",
             color = discord.Color.green()
        ))









keep_alive()
token = os.getenv("TOKEN")
bot.run(token)
