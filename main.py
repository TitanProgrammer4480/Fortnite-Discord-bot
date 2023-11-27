import discord
import os
import fortnite_api

token = os.getenv('TOKEN')
api_token = os.getenv("API_TOKEN")

api = fortnite_api.FortniteAPI(api_key=api_token)

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.command(description="Get Playerinfo")
async def player_info(
    ctx, player_name: discord.Option(discord.SlashCommandOptionType.string)):
    try:
        stats = api.stats.fetch_by_name(name=player_name)
    except:
        await ctx.respond("Player not found")
        return
    data = stats.raw_data
    #account info
    id = data["account"]["id"]
    name = data["account"]["name"]

    #battlepass info
    level = data["battlePass"]["level"]
    progress = data["battlePass"]["progress"]

    #overall info
    all_wins = data["stats"]["all"]["overall"]["wins"]
    all_kills = data["stats"]["all"]["overall"]["kills"]
    all_killsPerMin = data["stats"]["all"]["overall"]["killsPerMin"]
    all_killsPerMatch = data["stats"]["all"]["overall"]["killsPerMatch"]
    all_deaths = data["stats"]["all"]["overall"]["deaths"]
    all_kd = data["stats"]["all"]["overall"]["kd"]
    all_matches = data["stats"]["all"]["overall"]["matches"]
    all_winRate = data["stats"]["all"]["overall"]["winRate"]
    all_minutesPlayed = data["stats"]["all"]["overall"]["minutesPlayed"]
    all_playersOutlived = data["stats"]["all"]["overall"]["playersOutlived"]

    embed = discord.Embed(
        title=f"Stats from {name}",
        description=f"Fortnite stats from {name}",
        color=discord.Colour.blurple(),
    )
    embed.add_field(name="ID", value=id, inline=True)
    embed.add_field(name="name", value=name, inline=True)
    embed.add_field(name="level", value=level, inline=True)
    embed.add_field(name="progress", value=progress, inline=True)
    embed.add_field(name="all wins", value=all_wins, inline=True)
    embed.add_field(name="all kills", value=all_kills, inline=True)
    embed.add_field(name="Kills per min", value=all_killsPerMin, inline=True)
    embed.add_field(name="Kills per match",
                    value=all_killsPerMatch,
                    inline=True)
    embed.add_field(name="Deaths", value=all_deaths, inline=True)
    embed.add_field(name="KD", value=all_kd, inline=True)
    embed.add_field(name="Matches", value=all_matches, inline=True)
    embed.add_field(name="Win rate", value=all_winRate, inline=True)
    embed.add_field(name="Minutes played",
                    value=all_minutesPlayed,
                    inline=True)
    embed.add_field(name="Players outlived",
                    value=all_playersOutlived,
                    inline=True)

    embed.set_footer(text="")
    embed.set_author(
        name="ZonaryTitan",
        icon_url=
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpcCcQNUGyTpt1jjsWPZVrdEvPHO3kr7Tdg&usqp=CAU"
    )
    await ctx.respond("The stats:", embed=embed)


@bot.command(description="Sends the current map from Fortnite")
async def blank_map(ctx):
    map = api.map.fetch()
    data = map.raw_data

    map = data["images"]["blank"]

    embed = discord.Embed(
        title="The map",
        description="The map:",
        color=discord.Colour.blurple(),
    )
    embed.set_image(url=map)
    embed.set_footer(text="")
    embed.set_author(
        name="ZonaryTitan",
        icon_url=
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpcCcQNUGyTpt1jjsWPZVrdEvPHO3kr7Tdg&usqp=CAU"
    )
    await ctx.respond("The map:", embed=embed)


@bot.command(description="Sends the current map from Fortnite with pois")
async def map(ctx):
    map = api.map.fetch()
    data = map.raw_data

    map = data["images"]["pois"]

    embed = discord.Embed(
        title="The map",
        description="The map:",
        color=discord.Colour.blurple(),
    )
    embed.set_image(url=map)
    embed.set_footer(text="")
    embed.set_author(
        name="ZonaryTitan",
        icon_url=
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpcCcQNUGyTpt1jjsWPZVrdEvPHO3kr7Tdg&usqp=CAU"
    )
    await ctx.respond("The map:", embed=embed)


@bot.command(description="Sends all of the pois from the map")
async def pois(ctx):
    pois_data = api.map.fetch()
    data = pois_data.raw_data

    pois = data["pois"]

    embed = discord.Embed(
        title="The pois",
        description="The pois:",
        color=discord.Colour.blurple(),
    )
    for poi in pois:
        embed.add_field(
            name=poi["name"],
            value=
            f"x-position: {poi['location']['x']}, y-position: {poi['location']['x']}",
            inline=True)
    embed.set_footer(text="")
    embed.set_author(
        name="ZonaryTitan",
        icon_url=
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpcCcQNUGyTpt1jjsWPZVrdEvPHO3kr7Tdg&usqp=CAU"
    )
    await ctx.respond("The pois:", embed=embed)


@bot.command(description="Sends news from Fortnite")
async def compact_news(ctx):
    news_data = api.news.fetch()
    data = news_data.raw_data

    news = data["br"]["motds"]

    embed = discord.Embed(
        title="The news",
        description="The news:",
        color=discord.Colour.blurple(),
    )

    for new in news:
        embed.add_field(name=new["title"], value=new["body"], inline=True)

    embed.set_footer(text="")
    embed.set_author(
        name="ZonaryTitan",
        icon_url=
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpcCcQNUGyTpt1jjsWPZVrdEvPHO3kr7Tdg&usqp=CAU"
    )
    await ctx.respond("The news:", embed=embed)


@bot.command(description="Sends news from Fortnite")
async def news(ctx):
    news_data = api.news.fetch()
    data = news_data.raw_data

    news = data["br"]["motds"]

    for new in news:
        embed = discord.Embed(
            title="The news",
            description="The news:",
            color=discord.Colour.blurple(),
        )
        embed.add_field(name=new["title"], value=new["body"], inline=True)

        embed.set_image(url=new["image"])

        embed.set_footer(text="")
        embed.set_author(
            name="ZonaryTitan",
            icon_url=
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVpcCcQNUGyTpt1jjsWPZVrdEvPHO3kr7Tdg&usqp=CAU"
        )
        await ctx.respond("The news:", embed=embed)

bot.run(token)
