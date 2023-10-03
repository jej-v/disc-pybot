import discord
import random
from discord.commands import Option
from image_draw import senti, pinkuwu, pinkuwu_member

bot = discord.Bot()

# Just Quotes from taglines.txt on textfiles.com
with open('quotes.txt', 'r') as f:
    all_lines = f.readlines()

# Bot ON
@bot.event
async def on_ready():
    print('Bot is online!')


"""
    # supply the guild ids for the slash commands
    # if left empty, it will be considered as "public
    # slash command" and it will take up an hour to work.
"""
your_guild_ids_here = []

# ping
@bot.slash_command(guild_ids= your_guild_ids_here)
async def ping(ctx):
    """ping pong"""  # description
    await ctx.respond("Pong!")

# gae
@bot.slash_command(guild_ids= your_guild_ids_here)
async def gae(ctx):
    """How much gae can u have?"""  # description
    gae = randomint(1,10000)
    gae = gae / 100
    await ctx.respond(f"I see that you have **{gae}%**!!!")
    
# dice roller
@bot.slash_command(guild_ids= your_guild_ids_here)
async def dice(ctx):
    "Roll from 1 to 6, 7 if you're lucky"
    dice = random.randrange(1, 7)
    await ctx.respond(dice)
    
# quotes
@bot.slash_command(guild_ids= your_guild_ids_here)
async def q(ctx):
    """Just Quotes from taglines.txt on textfiles.com"""
    x = random.randint(0,len(all_lines)-1)
    await ctx.respond(all_lines[x])

# info command w option
@bot.slash_command(guild_ids= your_guild_ids_here)
async def info(
    ctx: discord.ApplicationContext,
    member: Option(discord.Member, "member", required=False)):
    """Shows info duh"""

    if member is None:
        member = ctx.author

    embed = discord.Embed(
        title = str(member.name) + "#" + str(member.discriminator),
        colour = discord.Colour.from_rgb(216, 195, 224)
        )

    embed.set_footer(text="A footer")
    embed.set_thumbnail(url= str(member.avatar))

    embed.add_field(name="Nickname:", value=str(member.display_name) ,inline=False)
    joined = member.joined_at # Month-Date-Year  Hour:Minute AM/PM
    embed.add_field(name="Joined this server at:", value=joined.strftime("%b-%d-%y %I:%M %p [UTC]"), inline=False)
    created = member.created_at # Month-Date-Year  Hour:Minute AM/PM
    embed.add_field(name="Account created at:", value=created.strftime("%b-%d-%y %I:%M %p [UTC]"), inline=False)
    embed.add_field(name="Is a bot?", value=str(member.bot) ,inline=False)

    await ctx.respond(embed=embed)

# choose
@bot.slash_command(guild_ids = your_guild_ids_here)
async def choose(
    ctx: discord.ApplicationContext,
    text: Option(str, "Enter your text")):
    """Let the Bot decide for you~"""

    author_name = ctx.author.name
    #split the text
    if ' or ' in text:
        options = text.split(' or ')
        decision = random.randint(0,len(options)-1)
        embed = discord.Embed(
            title = ":eyes: It's been decided, " + author_name,
            description = "I choose... **" + options[decision] + "**.",
            colour = discord.Colour.from_rgb(50, 205, 50)
        )
        await ctx.respond(embed=embed)

    else:
        await ctx.respond('I don\'t understand, ' + author_name + '. Usage: `/choose <option1> or <option2>`')

# uwu
@bot.slash_command(guild_ids = your_guild_ids_here)
async def uwu(
    ctx: discord.ApplicationContext,
    member: Option(discord.Member, "member", required=False)):
    """Uwus you or @Someone"""
    await ctx.respond("Uwuing......")

    if member is None:
        member = ctx.author

    url = str(member.avatar)
    pinkuwu_member(url)

    file = discord.File('uwout.png', filename='uwout.png')
    await ctx.edit(content=None, file=file)

# Yatta
@bot.slash_command(guild_ids = your_guild_ids_here)
async def yatta(
    ctx: discord.ApplicationContext,
    member: Option(discord.Member, "member", required=False)):
    """Get Yatta'd"""

    if member is None:
        member = ctx.author

    url = str(member.avatar)
    senti(url)
    await ctx.respond("Loading....")
    embed = discord.Embed (
        title = 'I will reverse all creations!',
        description = "",
        colour = discord.Colour.from_rgb(247, 168, 178)
    )

    file = discord.File("senti_result.png", filename="senti_result.png")
    embed.set_image(url="attachment://senti_result.png")
    embed.set_footer(text="Hacktoberfest 2022 <3")
    await ctx.edit(content=None, file=file, embed=embed)


# Help Command
@bot.slash_command(guild_ids= your_guild_ids_here)
async def help(ctx):
    """Shows the command list."""
    embed = discord.Embed(
        title = 'Command list',
        description = "Used to have a prefix ig",
        colour = discord.Colour.from_rgb(247, 168, 178)
    )

    embed.set_author(name = "Discord Python Bot", icon_url="https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png")
    embed.add_field(name="Standard Commands", value='''
`/help` - This message.
`/info` - I'll show your info.
`/info @Someone` - I'll show Someone's info.''', inline=False)
    embed.add_field(name="Fun Commands", value='''
`/ping` - Pong!
`/choose` - Let the Bot decide for you. Usage: `/choose <option1> or <option2>`
`/yatta` - Get Yatta'd
`/uwu` - Get Elysia'd
`/q` - I will say random quotes!''', inline=False)

    await ctx.respond(embed=embed)

# --Bot Token-- END
bot.run('your token')
