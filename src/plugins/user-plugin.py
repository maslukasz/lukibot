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

    await c.execute(f"SELECT xp, money, level FROM userdata WHERE userid = {event.author.id}")
    r = await c.fetchone()

    if r is None:
        await c.execute(f"INSERT INTO userdata(userid, xp, level, money, stars) VALUES({event.author.id}, 1, 1, 0, 0)")
        return

    new_xp = int(r[0] + random.randint(1, 3))
    new_money = int(r[1] + random.randint(1, 3))

    await c.execute(f"UPDATE userdata SET xp = {new_xp}, money = {new_money} WHERE userid = {event.author.id}")

    lvl_end = int(r[0] ** (1 / 4))
    level = int(r[2])
    print(lvl_end)
    print(level)

    level_up_msg = f'🎉 Gratulacje <@{event.message.author.id}>! Właśnie udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!'

    await c2.execute(f"SELECT * FROM leveling_roles WHERE guild = {event.get_guild().id}")
    leveling_roles_result = await c2.fetchall()

    for role in leveling_roles_result:
        await c.execute(f"SELECT role, level FROM leveling_roles WHERE level = {lvl_end} AND guild = {event.get_guild().id}")
        r = await c.fetchone()
        
    if str(lvl_end) in role:
        level_up_msg = f"""🎉 Gratulacje <@{event.message.author.id}>! Właśnie udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
:mirror_ball: Otrzymujesz <@&{role[1]}>!"""
        
    if level < lvl_end:
        await user_plugin.bot.rest.create_message(event.message.channel_id, hikari.Embed(title="Nowy poziom!", description=level_up_msg, colour="#2F3136"))
        await c.execute(f"UPDATE userdata SET level = {level+1} WHERE userid = {event.author.id}")
        return

def load(bot):
    bot.add_plugin(user_plugin)


def unload(bot):
    bot.remove_plugin(user_plugin) 

