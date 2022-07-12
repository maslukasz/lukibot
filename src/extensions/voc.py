import hikari
import lightbulb
import miru

import json

voc_plugin = lightbulb.Plugin("Slowka ")

@voc_plugin.command()
@lightbulb.option("", "text to repeat")
@lightbulb.command("echo", "repeats the given text")
@lightbulb.implements(lightbulb.PrefixCommand)
async def echo(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.text)


def load(bot):
    bot.add_plugin(voc_plugin)

def unload(bot):
    bot.remove_plugin(voc_plugin)
