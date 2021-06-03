import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot

# INTENTS ARE IMPORTANT.
bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())
# We will create our own help command.
bot.remove_command('help')

#Just Quotes from taglines.txt on textfiles.com
with open('quotes.txt', 'r') as f:
    all_lines = f.readlines()

# -- Bot events --
# Bot ON
@bot.event
async def on_ready():
    print('Bot is online!')

# To prevent spamming the cmd with CommandNotFound errors
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        pass

# Calls when a member leaves the server
@bot.event
async def on_member_remove(member):
    # Place Channel ID
   channel = bot.get_channel()
   name = member.name
   embed = discord.Embed(
    title = ":weary: " + name + " has left the server.",
    description = "Can we get Fs in the chat?",
    colour = discord.Colour.from_rgb(149, 125, 173)
   )
   embed.set_thumbnail(url= str(member.avatar_url))

   await channel.send(embed=embed)

@bot.event
async def on_message(message):
#!choose
    if message.content.startswith("!choose "):
        text = message.content[7:]
        member = message.author
        author_name = member.name
        #split the text
        if ' or ' in text:
            options = text.split(' or ')
            decision = random.randint(0,len(options)-1)

            embed = discord.Embed(
                title = ":eyes: It's been decided, " + author_name,
                description = "I choose... **" + options[decision] + "**.",
                colour = discord.Colour.from_rgb(188, 229, 226)
            )

            await message.channel.send(embed=embed)

        else:
            await message.channel.send('I don\'t understand, ' + author_name + '. Usage: `!choose <option1> or <option2>`')

#!info
    elif message.content.startswith("!info"):
        guild_id = message.guild
        if len(message.content) >= 6:
            try:
                member = discord.utils.get(message.guild.members, id=int(message.content[6:].strip('<>@!&')))
            except ValueError:
                await message.channel.send('I don\'t understand, ' + str(message.author.name) + '. Usage: `!info` or `!info @someone`')
        else:
            member = message.author

        embed = discord.Embed(
            title = str(member.name) + "#" + str(member.discriminator),
            colour = discord.Colour.from_rgb(216, 195, 224)
            )

        #embed.set_footer(text="A footer")
        embed.set_thumbnail(url= str(member.avatar_url))

        embed.add_field(name="Nickname:", value=str(member.display_name) ,inline=False)
        joined = member.joined_at # Month-Date-Year  Hour:Minute AM/PM
        embed.add_field(name="Joined this server at:", value=joined.strftime("%b-%d-%y %I:%M %p [UTC]"), inline=False)
        created = member.created_at # Month-Date-Year  Hour:Minute AM/PM
        embed.add_field(name="Account created at:", value=created.strftime("%b-%d-%y %I:%M %p [UTC]"), inline=False)
        embed.add_field(name="Is a bot?", value=str(member.bot) ,inline=False)

        await message.channel.send(embed=embed)

    else:
        pass

    await bot.process_commands(message)

# -- Bot commands --
#ping
@bot.command()
async def ping(ctx):
    await ctx.send(':ping_pong: Pong!')
#quotes
@bot.command()
async def q(ctx):
    x = random.randint(0,len(all_lines)-1)
    await ctx.send(all_lines[x])

#help
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Command list',
        description = "My prefix is `!`",
        colour = discord.Colour.from_rgb(247, 168, 178)
    )

    embed.set_author(name = "Discord Python Bot", icon_url="https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png")
    embed.add_field(name="Standard Commands", value='''
`!help` - This message.
`!info` - I'll show your info.
`!info @Someone` - I'll show Someone's info.''', inline=False)
    embed.add_field(name="Fun Commands", value='''
`!ping` - Pong!
`!q` I will say random quotes!
`!8ball` - Ask me anything!
`!choose` - Let me decide for you. Usage: `!choose <option1> or <option2> or..`''', inline=False)

    await ctx.send(embed=embed)

# # --Bot Token-- END
bot.run('')
