import hikari
import lightbulb

import psycopg2

stats_plugin = lightbulb.Plugin("Plugin stats_plugin")

con = psycopg2.connect(
        host="localhost",
        dbname="demo",
        user='postgres',
        password='admin',
        port=5432)
    
c = con.cursor()


#@stats_plugin.listener(hikari.GuildMessageCreateEvent)
#async def leveling(event: hikari.Event) -> None:
#    pass




def load(bot):
    bot.add_plugin(stats_plugin)

def unload(bot):
    bot.remove_plugin(stats_plugin)

