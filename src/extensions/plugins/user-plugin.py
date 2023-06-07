import hikari
import lightbulb

import random
import datetime

user_plugin = lightbulb.Plugin("Plugin użytkownika")

@user_plugin.listener(hikari.GuildMessageCreateEvent)
async def leveling(event: hikari.Event) -> None:
    if event.author.is_bot or event.message.channel_id == 688507273198436385 or event.message.channel_id == 779275734707077130 or event.message.channel_id == 734518823188824114:
        return
        
    async with user_plugin.bot.d.db.acquire() as con:
        c = await con.cursor()
        c2 = await con.cursor()
        c3 = await con.cursor()

    await c.execute(f"SELECT xp, level FROM userdata WHERE user_id = {event.author.id} AND guild_id = {event.get_guild().id}")
    r = await c.fetchone()

    if r is None:
        await c.execute(f"INSERT INTO userdata(guild_id, user_id, xp, level, partnerships) VALUES({event.get_guild().id}, {event.author.id}, 1, 1, 0)")
        return

    await c3.execute(f"SELECT xp_system FROM config_values WHERE guild_id = {event.get_guild().id}")
    r3 = await c3.fetchone()

    if r3 is None:
        await c3.execute(f"INSERT INTO config_values(guild_id, xp_system) VALUES ({event.get_guild().id}, False)")
    
    if r3[0] == 0:
        return

    new_xp = int(r[0] + random.randint(1, 3))

    await c.execute(f"UPDATE userdata SET xp = {new_xp} WHERE user_id = {event.author.id} AND guild_id = {event.get_guild().id}")

    lvl_end = int(r[0] ** (1 / 4))
    level = int(r[1])

    level_up_msg = f'<:TE_Event:1111739449794105536> Gratulacje <@{event.message.author.id}>! Właśnie udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!'

    await c2.execute(f"SELECT * FROM leveling_roles WHERE guild = {event.get_guild().id}")
    leveling_roles_result = await c2.fetchall()
            
    if level < lvl_end:
        await c.execute(f"SELECT role, level FROM leveling_roles WHERE level = {lvl_end} AND guild = {event.get_guild().id}")
        r = await c.fetchone()
        if r is not None:
            await event.get_member().add_role(int(r[0]))
            level_up_msg = f"""<:TE_Event:1111739449794105536> Gratulacje <@{event.message.author.id}>! Właśnie udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
<:TE_Plus:1111972941467488306> Otrzymujesz <@&{r[0]}>!"""
        await user_plugin.bot.rest.create_message(event.message.channel_id, hikari.Embed(title="Nowy poziom!", description=level_up_msg, colour="#2F3136"))
        await c.execute(f"UPDATE userdata SET level = {level+1} WHERE user_id = {event.author.id} AND guild_id = {event.get_guild().id}")
        return

def load(bot):
    bot.add_plugin(user_plugin)


def unload(bot):
    bot.remove_plugin(user_plugin) 

