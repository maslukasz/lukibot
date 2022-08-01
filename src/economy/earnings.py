import hikari
import lightbulb

earnings_plugin = lightbulb.Plugin("Rawki", "Plugin z gotowymi komendami")

@earnings_plugin.command
@lightbulb.command("work", "work")
@lightbulb.implements(lightbulb.PrefixCommand)
async def raw(ctx: lightbulb.Context) -> None:
    await ctx.respond("temp")
        
        

def load(bot):
    bot.add_plugin(earnings_plugin)

def unload(bot):
    bot.remove_plugin(earnings_plugin)