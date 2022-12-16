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

    await c.execute(f"SELECT xp, money, level FROM userdata WHERE userid = {event.author.id}")
    r = await c.fetchone()

    if r is None:
        await c.execute(f"INSERT INTO userdata(userid, xp, level, money, stars) VALUES({event.author.id}, 1, 1, 0, 0)")
        return

    new_xp = int(r[0] + random.randint(1, 3))
    new_money = int(r[1] + random.randint(1, 3))

    await c.execute(f"UPDATE userdata SET xp = {new_xp}, money = {new_money} WHERE userid = {event.author.id}")

    user = user_plugin.bot.cache.get_member(event.get_guild(), event.member.id)
    roles = (await user.fetch_roles())

    def role_check(role_id):
        for role in roles:
            print(role.id)
            if role.id == role_id:
                print("działa")
                break

    lvl_end = int(r[0] ** (1 / 4))
    level = int(r[2])
    level_up_msg = f'🎉 Gratulacje <@{event.message.author.id}>! Właśine udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!'

    if lvl_end == 5:
        role_check(630489950009294897)
        await user_plugin.bot.rest.add_role_to_member(guild=event.get_guild().id, user=event.member.id, role=630489950009294897)
        level_up_msg = f"""🎉 Gratulacje <@{event.message.author.id}>! Właśine udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
:mirror_ball: Otrzymujesz <@&630489950009294897>!"""

    if lvl_end == 10:
        await user_plugin.bot.rest.add_role_to_member(guild=event.get_guild().id, user=event.member.id, role=630489979734327323)
        await user_plugin.bot.rest.remove_role_from_member(630489979734327323)
        level_up_msg = f"""🎉 Gratulacje <@{event.message.author.id}>! Właśine udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
:mirror_ball: Otrzymujesz <@&630489979734327323>!
:wastebasket: Zabieram <@&630489979734327323>"""

    if lvl_end == 15:
        await user_plugin.bot.rest.add_role_to_member(guild=event.get_guild().id, user=event.member.id, role=630490054321635368)
        await user_plugin.bot.rest.remove_role_from_member(630490054321635368)
        level_up_msg = f"""🎉 Gratulacje <@{event.message.author.id}>! Właśine udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
:mirror_ball: Otrzymujesz <@&630490054321635368>!
:wastebasket: Zabieram <@&630490054321635368>"""
    
    if lvl_end == 20:
         await user_plugin.bot.rest.add_role_to_member(guild=event.get_guild().id, user=event.member.id, role=724323821313589290)
         await user_plugin.bot.rest.remove_role_from_member(724323821313589290)
         level_up_msg = f"""🎉 Gratulacje <@{event.message.author.id}>! Właśine udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
:mirror_ball: Otrzymujesz <@&724323821313589290>!
:wastebasket: Zabieram <@&724323821313589290>"""
    
    if lvl_end == 25:
         await user_plugin.bot.rest.add_role_to_member(guild=event.get_guild().id, user=event.member.id, role=688363696602349579)
         await user_plugin.bot.rest.remove_role_from_member(688363696602349579)
         level_up_msg = f"""🎉 Gratulacje <@{event.message.author.id}>! Właśine udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
:mirror_ball: Otrzymujesz <@&688363696602349579>!
:wastebasket: Zabieram <@&688363696602349579>"""

    if lvl_end == 30:
         await user_plugin.bot.rest.add_role_to_member(guild=event.get_guild().id, user=event.member.id, role=688363696291971146)
         await user_plugin.bot.rest.remove_role_from_member(688363696291971146)
         level_up_msg = f"""🎉 Gratulacje <@{event.message.author.id}>! Właśine udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
:mirror_ball: Otrzymujesz <@&688363696291971146>!
:wastebasket: Zabieram <@&688363696602349579>"""

    if lvl_end == 35:
         await user_plugin.bot.rest.add_role_to_member(guild=event.get_guild().id, user=event.member.id, role=688363695461629981)
         await user_plugin.bot.rest.remove_role_from_member(688363695461629981)
         level_up_msg = f"""🎉 Gratulacje <@{event.message.author.id}>! Właśine udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
:mirror_ball: Otrzymujesz <@&688363695461629981>!
:wastebasket: Zabieram <@&688363696291971146>"""

    if lvl_end == 40:
         await user_plugin.bot.rest.add_role_to_member(guild=event.get_guild().id, user=event.member.id, role=688363695461629981)
         await user_plugin.bot.rest.remove_role_from_member(688363695461629981)
         level_up_msg = f"""🎉 Gratulacje <@{event.message.author.id}>! Właśine udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
:mirror_ball: Otrzymujesz <@&688363695461629981>!
:wastebasket: Zabieram <@&688363695461629981>"""

    if lvl_end == 45:
         await user_plugin.bot.rest.add_role_to_member(guild=event.get_guild().id, user=event.member.id, role=688363695109046295)
         await user_plugin.bot.rest.remove_role_from_member(688363695109046295)
         level_up_msg = f"""🎉 Gratulacje <@{event.message.author.id}>! Właśine udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
:mirror_ball: Otrzymujesz <@&688363695109046295>!
:wastebasket: Zabieram <@&688363695461629981>"""

    if lvl_end == 50:
         await user_plugin.bot.rest.add_role_to_member(guild=event.get_guild().id, user=event.member.id, role=688363695042199552)
         await user_plugin.bot.rest.remove_role_from_member(688363695042199552)
         level_up_msg = f"""🎉 Gratulacje <@{event.message.author.id}>! Właśine udało Ci się zdobyć **{lvl_end}** poziom. Oby tak dalej!
:mirror_ball: Otrzymujesz <@&688363695042199552>!
:wastebasket: Zabieram <@&688363695109046295>"""


    if level < lvl_end:
        await user_plugin.bot.rest.create_message(event.message.channel_id, hikari.Embed(title="Nowy poziom!", description=level_up_msg, colour="#2F3136"))
        await c.execute(f"UPDATE userdata SET level = {level+1} WHERE userid = {event.author.id}")

def load(bot):
    bot.add_plugin(user_plugin)


def unload(bot):
    bot.remove_plugin(user_plugin) 

