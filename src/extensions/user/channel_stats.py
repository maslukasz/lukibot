import hikari
import lightbulb
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import datetime

import time

channel_stats_extension = lightbulb.Plugin("channel_stats_extension", "Plugin z gotowymi komendami")

@channel_stats_extension.command
@lightbulb.command('today-messages', 'info o kanale', aliases=['today', 'tm'])
@lightbulb.implements(lightbulb.PrefixCommand)
async def channel_stats(ctx: lightbulb.Context) -> None:
    async with channel_stats_extension.bot.d.db.acquire() as con:
        c = await con.cursor()
        c2 = await con.cursor()
        c3 = await con.cursor()
        c4 = await con.cursor()

    await c.execute(f'SELECT sum(messages) from history_users WHERE data = date(now()) AND guild_id = {ctx.get_guild().id}')
    r = await c.fetchone()

    await c2.execute(f"SELECT DISTINCT sum(messages), user_id from history_users WHERE data = date(now()) AND guild_id = {ctx.get_guild().id} GROUP BY user_id ORDER BY sum(messages) DESC")
    r2 = await c2.fetchall()

    await c3.execute(f"SELECT DISTINCT sum(messages), channel from history_users WHERE data = date(now()) AND guild_id = {ctx.get_guild().id} GROUP BY channel ORDER BY sum(messages) DESC")
    r3 = await c3.fetchall()
    print(r3)

    chart = []
    ids = []
    for msg, id in r2:
        asd = channel_stats_extension.bot.cache.get_user(id)
        ids.append(asd)
        chart.append(int(msg))

    
    plt.style.use('ggplot')
    plt.style.use('Solarize_Light2')

    plt.pie(chart, labels=ids, autopct='%1.1f%%', radius=1.2)
    plt.savefig("tm.png")
    plt.close()

    top3 = "Minimum 3 osoby muszą wysłać wiadomość, żeby pokazała się topka!"

    if len(r2) < 3:
        top3chan = " "
    else:
        top3 = f"""🤓 **Najaktywniejsi dzisiaj**
🥇 <@{r2[0][1]}> ({r2[0][0]})
🥈 <@{r2[1][1]}> ({r2[1][0]})
🥉 <@{r2[2][1]}> ({r2[2][0]})"""

    top3chan = " "

    if len(r3) < 3:
        top3chan = "Musi się pojawić minimum 1 wiadomość na 3 kanałach, żeby pokazała się topka!"
    else:
        top3chan = f"""📁 **Najaktywniejsze kanały**
🥇 <#{r3[0][1]}> ({r3[0][0]})
🥈 <#{r3[1][1]}> ({r3[1][0]})
🥉 <#{r3[2][1]}> ({r3[2][0]})"""

    embed = hikari.Embed(description=f"""> <:blue_shocked:1057762095036387328> Dzisiaj napisano **{r[0]}** wiadomości!
    
{top3}

{top3chan}""", color='#3475ff')
    embed.set_image("tm.png")
    await ctx.respond(embed=embed)


@channel_stats_extension.command
@lightbulb.command('serwer', 'info o kanale')
@lightbulb.implements(lightbulb.PrefixCommand)
async def asd(ctx: lightbulb.Context) -> None:
    async with channel_stats_extension.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT DISTINCT sum(messages), data FROM history_users WHERE data BETWEEN DATE_ADD(now(), INTERVAL -14 day) AND date(now()) AND guild_id = {ctx.get_guild().id} GROUP BY data LIMIT 14")
    r = await c.fetchall()

    plt.style.use('ggplot')
    plt.style.use('Solarize_Light2')

    chart = []
    daty = []
    for msg, data in r:
        chart.append(msg)
        daty.append(str(data[8:]))

    plt.stem(daty, chart)
    plt.savefig("schart.png")
    plt.close()

    embed = hikari.Embed(description=f"""📆 Wykres wiadomości z ostatnich **14 dni**""", color='#3475ff')
    embed.set_image("schart.png")
    await ctx.respond(embed=embed)


@channel_stats_extension.command
@lightbulb.command('me', 'info o kanale')
@lightbulb.implements(lightbulb.PrefixCommand)
async def channel_stats(ctx: lightbulb.Context) -> None:
    async with channel_stats_extension.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT DISTINCT sum(messages), guild_id FROM history_users WHERE user_id = {ctx.author.id} GROUP BY guild_id")
    r = await c.fetchall()

    msgs = []
    guild_id = []
    for msg, data in r:
        msgs.append(msg)
        asd = channel_stats_extension.bot.cache.get_guild(data)
        guild_id.append(asd)

    plt.style.use('ggplot')
    #plt.style.use('Solarize_Light')
    
    plt.pie(msgs, labels=guild_id, autopct='%1.1f%%')
    plt.savefig("me.png")
    plt.close()

    strs = ' '
    for i in range(len(r)):
        serwer = channel_stats_extension.bot.cache.get_guild(r[i][1])
        strs += f'<:blurpledot:925702134467551273> {serwer} - **{msgs[i]}** wiadomości\n'
        print(len(strs)) 
    
    embed = hikari.Embed(description=f"""Twoja łączna ilość wiadomości na serwerach, gdzie dodany jest **[lukibot](https://discord.gg/Khj2Rj2qeT)**.

{strs}""", color='#3475ff')
    embed.set_image("me.png")
    await ctx.respond(embed=embed)
def load(bot):
    bot.add_plugin(channel_stats_extension)

def unload(bot):
    bot.remove_plugin(channel_stats_extension)
