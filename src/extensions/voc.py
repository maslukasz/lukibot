import hikari
import lightbulb
import miru
from miru.ext import nav

import json

voc_plugin = lightbulb.Plugin("Slowka ")

# @voc_plugin.command()
# @lightbulb.option("color", "Kolor", required=False, default='#7289da')
# @lightbulb.option("description", "Główny tekst")
# @lightbulb.option("title", "Nagłówek")
# @lightbulb.command("echo", "repeats the given text")
# @lightbulb.implements(lightbulb.SlashCommand)
# async def echo(ctx: lightbulb.Context, ) -> None:
#     async with voc_plugin.bot.d.db.acquire() as con:
#         c = await con.cursor()

#     await c.execute(f"""INSERT INTO embeds(guild_id, author_id, content, colour, title) VALUES(
#         {ctx.get_guild().id},
#         {ctx.author.id},
#         {ctx.options.description},
#         {ctx.options.color},
#         {ctx.options.title})""")

#     await ctx.respond(hikari.Embed(title=ctx.options.title, description=ctx.options.description, color=ctx.options.color))


def load(bot):
    bot.add_plugin(voc_plugin)

def unload(bot):
    bot.remove_plugin(voc_plugin)
