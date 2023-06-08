import hikari
import lightbulb

import numpy as np
import plotly.graph_objects as go

from datetime import datetime

channel_stats_extension = lightbulb.Plugin("channel_stats_extension", "Plugin z gotowymi komendami")

@channel_stats_extension.command
@lightbulb.command('today-messages', 'Dzisiejsze statystyki tekstowe.', aliases=['today', 'tm'])
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def channel_stats(ctx: lightbulb.Context) -> None:
    async with channel_stats_extension.bot.d.db.acquire() as con:
        c = await con.cursor()
        
    await c.execute(f'SELECT sum(messages) from history_users WHERE data = date(now()) AND guild_id = {ctx.get_guild().id}')
    r = await c.fetchone()

    await c.execute(f"SELECT DISTINCT sum(messages), user_id from history_users WHERE data = date(now()) AND guild_id = {ctx.get_guild().id} GROUP BY user_id ORDER BY sum(messages) DESC")
    r2 = await c.fetchall()

    await c.execute(f"SELECT DISTINCT sum(messages), channel from history_users WHERE data = date(now()) AND guild_id = {ctx.get_guild().id} GROUP BY channel ORDER BY sum(messages) DESC")
    r3 = await c.fetchall()

    chart_values = []
    users_ids = []

    message = await ctx.respond(hikari.Embed(title='<:TE_Search:1111737067995668602> Zbieranie danych...', color='#00ff00'))
    
    for msg, id in r2:
        user = channel_stats_extension.bot.cache.get_user(id)
        if user is not None:
            users_ids.append(user.username)
        chart_values.append(int(msg))

    fig = go.Figure(data=[go.Pie(labels=users_ids, values=chart_values, textinfo='label+percent', showlegend=False)])
    fig.update_layout(margin=dict(l=50, r=10, b=10, t=20))
    fig.write_image('./src/img/tm.png')

    top3 = "<:nie:866036882553700353> Minimum 3 osoby muszą wysłać wiadomość, żeby pokazała się topka!"

    if len(r2) < 3:
        top3chan = " "
    else:
        top3 = f"""<:TE_Members:1111738982305370153> **Najaktywniejsi dzisiaj**
🥇 <@{r2[0][1]}> ({r2[0][0]})
🥈 <@{r2[1][1]}> ({r2[1][0]})
🥉 <@{r2[2][1]}> ({r2[2][0]})"""

    top3chan = " "

    if len(r3) < 3:
        top3chan = "<:nie:866036882553700353> Musi się pojawić minimum 1 wiadomość na 3 kanałach, żeby pokazała się topka!"
    else:
        top3chan = f"""<:TE_Assets:1111740692771913768> **Najaktywniejsze kanały**
🥇 <#{r3[0][1]}> ({r3[0][0]})
🥈 <#{r3[1][1]}> ({r3[1][0]})
🥉 <#{r3[2][1]}> ({r3[2][0]})"""

    embed = hikari.Embed(description=f"""## Napisano dziś [**{r[0]}**](https://discord.gg/Khj2Rj2qeT) wiadomości!
{top3}

{top3chan}""", color='#3475ff')
    embed.set_image("./src/img/tm.png")
    await message.edit(embed=embed)


@channel_stats_extension.command
@lightbulb.command('server', 'Statystyki serwera z ostatnich 14 dni.', aliases=['server'])
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def user(ctx: lightbulb.Context) -> None:
    async with channel_stats_extension.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT DISTINCT sum(messages), data FROM history_users WHERE data BETWEEN DATE_ADD(now(), INTERVAL -14 day) AND date(now()) AND guild_id = {ctx.get_guild().id} GROUP BY data LIMIT 14")
    r = await c.fetchall()

    message = await ctx.respond(hikari.Embed(title='<:TE_Search:1111737067995668602> Zbieranie danych...', color='#00ff00'))

    chart_values = []
    daty = []
    
    for msg, data in r:
        chart_values.append(msg)
        daty.append(str(data[8:]))

    fig = go.Figure(data=go.Scatter(x=daty, y=chart_values, line=dict(color='blue', width=2)))
    fig.update_layout(margin=dict(l=50, r=10, b=10, t=10))
    fig.write_image('./src/img/schart.png')

    embed = hikari.Embed(description=f"""📆 Wykres wiadomości z ostatnich **14 dni**""", color='#3475ff')
    embed.set_image("./src/img/schart.png")
    embed.set_footer(text='Jeśli w jakimś dniu było 0 wiadomości, to jest on pomijany.', icon='https://cdn.discordapp.com/emojis/1111741159186907317.webp?size=96&quality=lossless')
    await message.edit(embed=embed)


@channel_stats_extension.command
@lightbulb.command('server-stats', 'Twoje statystyki z serwerów na których jest bot.', aliases=['me'])
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def channel_stats(ctx: lightbulb.Context) -> None:
    async with channel_stats_extension.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT DISTINCT sum(messages), guild_id FROM history_users WHERE user_id = {ctx.author.id} GROUP BY guild_id")
    r = await c.fetchall()

    message = await ctx.respond(hikari.Embed(title='<:TE_Search:1111737067995668602> Zbieranie danych...', color='#00ff00'))

    messages = []
    guilds = []
    for msg, data in r:
        messages.append(msg)
        guild = channel_stats_extension.bot.cache.get_guild(data)
        guilds.append(guild.name)

    fig = go.Figure(data=[go.Pie(labels=guilds, values=messages, textinfo='label+percent', showlegend=False)])
    fig.update_layout(margin=dict(l=50, r=10, b=10, t=20))
    fig.write_image('./src/img/me.png')
    
    stats = ' '
    for i in range(len(r)):
        serwer = channel_stats_extension.bot.cache.get_guild(r[i][1])
        stats += f'<:TE_Dot:1111753885950955560> {serwer} - **{messages[i]}** wiadomości\n'
    
    embed = hikari.Embed(description=f"""<:TE_Messages:1111737448582631424> Twoja łączna ilość wiadomości na serwerach, gdzie dodany jest **[lukibot](https://discord.gg/Khj2Rj2qeT)**.

{stats}""", color='#3475ff')
    embed.set_image("./src/img/me.png")
    await message.edit(embed=embed)
def load(bot):
    bot.add_plugin(channel_stats_extension)

def unload(bot):
    bot.remove_plugin(channel_stats_extension)
