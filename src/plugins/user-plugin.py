import hikari
import lightbulb

import random
import psycopg2

user_plugin = lightbulb.Plugin("Plugin użytkownika")

con = psycopg2.connect(
        host="localhost",
        dbname="demo",
        user='postgres',
        password='admin',
        port=5432)
    
c = con.cursor()

cooldown_manager = lightbulb.CooldownManager(lambda _: lightbulb.UserBucket(5, 1))
@user_plugin.listener(hikari.GuildMessageCreateEvent)
async def leveling(event: hikari.Event) -> None:
    if event.author.is_bot or event.message.channel_id == 688507273198436385 or event.message.channel_id == 779275734707077130 or event.message.channel_id == 734518823188824114:
        return

    c.execute(f"SELECT xp, level, messages7d, messages30d  FROM userdata WHERE userid = {event.author.id}")
    r = c.fetchone()

    if r is None:
        sql = "INSERT INTO userdata(userid, xp, level, messages7d, messages30d) VALUES (%s, %s, %s, %s, %s)"
        val = (event.member.id, 0, 0, 0, 0)
        c.execute(sql, val)
        con.commit()
        await user_plugin.app.rest.create_message(874675093354201148, hikari.Embed(
            title="Zarejestrowano nowego użytkownika",
            description=f"""Użytkownik <@{event.member.id}> ({event.member.id}) właśnie został zarejestrowany w bazie danych.
            
💾 **Wpisane dane:**
ID: `{event.member.id}`
XP: `0`
Level: `0`""", colour="#00ff00"))
        return
    
    messages = int(r[2])
    newmessages = int(messages + 1)
    print(messages)

    c.execute(f"UPDATE userdata SET messages = {newmessages} WHERE userid = {event.author.id}")

    context = await user_plugin.app.get_prefix_context(event)
    if getattr(context, "command", None) is not None:
        return

    context = lightbulb.PrefixContext(user_plugin.app, event, None, "", "")
    try: #dodawanie cooldownu do contextu
        await cooldown_manager.add_cooldown(context)
    except lightbulb.CommandIsOnCooldown: # nie dodawanie XP, jesli cooldown dalej trwa
        return

    else:
        xp = r[0]
        lvl = r[1]
        
        gainxp = random.randint(1,3)
        newxp = int(xp + gainxp)
        print(newxp)

        c.execute(f"UPDATE userdata SET xp = {newxp} WHERE userid = {event.author.id}")

        lvl_end = int(xp ** (1/3))
        if lvl < lvl_end:
            c.execute(f"UPDATE userdata SET level = {lvl+1} WHERE userID = {event.author.id}")
            await user_plugin.app.rest.create_message(874675093354201148, hikari.Embed(
            title="Nowy poziom",
            description=f"""Użytkownik <@{event.member.id}> właśnie zdobył/-a **{lvl+1}** poziom. Gratulacje!""", colour="#00ff00"))
        
    con.commit()

def load(bot):
    bot.add_plugin(user_plugin)


def unload(bot):
    bot.remove_plugin(user_plugin)

