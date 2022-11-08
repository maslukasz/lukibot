import hikari
import lightbulb

import datetime
import time
import random

earnings_plugin = lightbulb.Plugin("Rawki", "Plugin z gotowymi komendami")

@earnings_plugin.command
@lightbulb.command("work", "work")
@lightbulb.implements(lightbulb.PrefixCommand)
async def work(ctx: lightbulb.Context) -> None:
    async with earnings_plugin.bot.d.db.acquire() as con:
        c = await con.cursor()
    await c.execute(f"SELECT work FROM cooldowns WHERE userid = {ctx.author.id}")
    r = await c.fetchone()

    if r is None:
        await c.execute(f"INSERT INTO cooldowns (userid, work) VALUES ({ctx.author.id}, timestamp(now()))")
        await ctx.respond(hikari.Embed(description=f'<:nie:783659534455275560> Nie było Cię w bazie danych. Spróbuj jeszcze raz.', color='#ff0000'))
        return

    if r[0] > str(datetime.datetime.now()):
        await c.execute(f"""SELECT work, CASE
        WHEN work IS NOT NULL THEN unix_timestamp(work)
        END FROM cooldowns WHERE userid = {ctx.author.id}""")
        r = await c.fetchone()
        await ctx.respond(hikari.Embed(description=f'<:nie:783659534455275560> Jeszcze nie możesz użyć komendy. Będzie to możliwe za <t:{int(r[1])}:R>.', color='#ff0000'))
        return
    else:
        await c.execute(f"SELECT money FROM userdata WHERE userid = {ctx.author.id}")
        r = await c.fetchone()

        earn = random.randint(10, 100)
        new_money = r[0] + earn

        await c.execute(f"UPDATE userdata SET money = {new_money} WHERE userid = {ctx.author.id}")
        await c.execute(f"UPDATE cooldowns SET work = date_add(now(), interval 2 hour) WHERE userid = {ctx.author.id}")
        work_reply = [f'Skomponowałeś/aś utwór do gry. Deweloper dał Ci **{earn}** <:thend:742800976636936202> wynagrodzenia.', f'Ładnie odkurzyłeś/-aś pokój. Mama dała Ci za to **{earn}** <:thend:742800976636936202>.', f'Pomogłeś/-aś starszej Pani przejść przez pasy. Dała Ci za pomoc **{earn}** <:thend:742800976636936202>.', f'Zgłosiłeś delikwenta, który reklamował się w prywatnej wiadomości. Administracja dała Ci za to **{earn}** <:thend:742800976636936202>.', f"Założyłeś się ze znajomymi, że uda Ci się ugrać clutch'a 1 na 5 w csie. Dali Ci za to **{earn}** <:thend:742800976636936202>."]
        await ctx.respond(hikari.Embed(description=random.choice(work_reply), colour='#4F545C'))
        
        

def load(bot):
    bot.add_plugin(earnings_plugin)

def unload(bot):
    bot.remove_plugin(earnings_plugin)
