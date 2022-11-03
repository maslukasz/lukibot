import hikari
import lightbulb


stats_plugin = lightbulb.Plugin("Plugin stats_plugin")


#@stats_plugin.listener(hikari.GuildMessageCreateEvent)
#async def leveling(event: hikari.Event) -> None:
#    pass




def load(bot):
    bot.add_plugin(stats_plugin)

def unload(bot):
    bot.remove_plugin(stats_plugin)

