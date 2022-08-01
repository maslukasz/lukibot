import hikari
import lightbulb

import sqlite3 as db
con = db.connect('main.db')
c = con.cursor()

user_plugin = lightbulb.Plugin("Rawki", "Plugin z gotowymi komendami")

@user_plugin.command
@lightbulb.command("profile", "raw group")
@lightbulb.implements(lightbulb.PrefixCommand)
async def profile(ctx: lightbulb.Context) -> None:
    c.execute("SELECT")
    
        

def load(bot):
    bot.add_plugin(user_plugin)

def unload(bot):
    bot.remove_plugin(user_plugin)