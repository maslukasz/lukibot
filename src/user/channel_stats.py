import hikari
import lightbulb
import numpy as np

import time

channel_stats_extension = lightbulb.Plugin("channel_stats_extension", "Plugin z gotowymi komendami")

@channel_stats_extension.command
@lightbulb.option('id', 'channel id', required=False)
@lightbulb.command('channel-stats', 'info o kanale')
@lightbulb.implements(lightbulb.PrefixCommand)
async def channel_stats(ctx: lightbulb.Context) -> None:
    async with channel_stats_extension.bot.d.db.acquire() as con:
        c = await con.cursor()
    
    if ctx.options.id is None:
        await ctx.respond("Brak id")
        return

    await c.execute(f"SELECT userid, SUM(messages) FROM history_users WHERE channel = {ctx.options.id} GROUP BY messages LIMIT 5")
    r = await c.fetchall()

    await ctx.respond(hikari.Embed(description=f"""🥇 **
<:blurpledot:925702134467551273>
<:blurpledot:925702134467551273>"""))

    print(r)

    await ctx.respond(r)


@channel_stats_extension.command
@lightbulb.command('me', 'info o kanale')
@lightbulb.implements(lightbulb.PrefixCommand)
async def asd(ctx: lightbulb.Context) -> None:
    if ctx.author.id.created_at.timestamp() > int(time.time()):
        await ctx.respond("test")
    else:
        await ctx.respond("tetg2")

def load(bot):
    bot.add_plugin(channel_stats_extension)

def unload(bot):
    bot.remove_plugin(channel_stats_extension)
