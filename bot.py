from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!')
token = "ODQ4MTQ1NzIyMTI5MzgzNDM1.YLIXQQ.9QAPx5L62mAqsPiupeVuFYddKJ0"

@bot.command()
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await user.send(message)

bot.run(token)