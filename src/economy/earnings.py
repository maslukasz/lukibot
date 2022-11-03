import hikari
import lightbulb

import datetime
import random

import sqlite3 as db
con = db.connect('main.db')
c = con.cursor()
c2 = con.cursor()

earnings_plugin = lightbulb.Plugin("Rawki", "Plugin z gotowymi komendami")

@earnings_plugin.command
@lightbulb.command("work", "work")
@lightbulb.implements(lightbulb.PrefixCommand)
async def work(ctx: lightbulb.Context) -> None:
    c.execute(f"SELECT work FROM cooldowns WHERE userid = {ctx.author.id}")
    r = c.fetchone()

    if r is None:
        c.execute(f"INSERT INTO cooldowns (userid, work) VALUES ({ctx.author.id}, datetime('now', 'localtime', '+2 hours'))")
        con.commit()
        return

    if r[0] > str(datetime.datetime.now()):
        c.execute("SELECT work, strftime('%s', work) FROM cooldowns WHERE userid = 342355402429825035")
        r = c.fetchone()
        await ctx.respond(hikari.Embed(description=f'<:nie:783659534455275560> Jeszcze nie możesz użyć komendy. Będzie to możliwe za <t:{r[1]}:R>.', color='#ff0000'))
        return
    else:
        c.execute(f"SELECT money FROM userdata WHERE userid = {ctx.author.id}")
        r = c.fetchone()

        earn = random.randint(10, 100)
        new_money = r[0] + earn

        c.execute(f"UPDATE userdata SET money = {new_money} WHERE userid = {ctx.author.id}")
        con.commit()
        work_reply = [f'Skomponowałeś/aś utwór do gry. Deweloper dał Ci **{earn}** <:thend:742800976636936202> wynagrodzenia.', f'Ładnie odkurzyłeś/-aś pokój. Mama dała Ci za to **{earn}** <:thend:742800976636936202>.', f'Pomogłeś/-aś starszej Pani przejść przez pasy. Dała Ci za pomoc **{earn}** <:thend:742800976636936202>.', f'Zgłosiłeś delikwenta, który reklamował się w prywatnej wiadomości. Administracja dała Ci za to **{earn}** <:thend:742800976636936202>.', f"Założyłeś się ze znajomymi, że uda Ci się ugrać clutch'a 1 na 5 w csie. Dali Ci za to **{earn}** <:thend:742800976636936202>."]
        await ctx.respond(hikari.Embed(description=random.choice(work_reply), colour='#4F545C'))
        
        

def load(bot):
    bot.add_plugin(earnings_plugin)

def unload(bot):
    bot.remove_plugin(earnings_plugin)
