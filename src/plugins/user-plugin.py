import hikari
import lightbulb

import random
import datetime

user_plugin = lightbulb.Plugin("Plugin użytkownika")

import aiomysql

@user_plugin.listener(hikari.GuildMessageCreateEvent)
async def leveling(event: hikari.Event) -> None:
    if event.author.is_bot or event.message.channel_id == 688507273198436385 or event.message.channel_id == 779275734707077130 or event.message.channel_id == 734518823188824114:
        return
        
    async with user_plugin.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT * FROM userdata WHERE userid = {event.author.id}")
    r = await c.fetchone()
    
    if r is None:
        await c.execute(f"INSERT INTO userdata(userid, xp, level, money, stars) VALUES({event.author.id}, 1, 1, 0, 0)")
        return


def load(bot):
    bot.add_plugin(user_plugin)


def unload(bot):
    bot.remove_plugin(user_plugin)

