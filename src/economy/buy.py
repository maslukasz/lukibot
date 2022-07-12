import hikari 
import lightbulb

import psycopg2

con = psycopg2.connect(
        host="localhost",
        dbname="demo",
        user='postgres',
        password='admin',
        port=5432)
    
c = con.cursor()

buy_ext = lightbulb.Plugin("buy", "buy")

@buy_ext.command
@lightbulb.command('buy', 'buy command', aliases=['kup'])
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def but(ctx: lightbulb.Context) -> None:
    c.execute(f'SELECT money FROM userdata WHERE userid = {ctx.member.id}')
    r = c.fetchone()
    if r is None:
        sql = "INSERT INTO userdata(userid, xp, level, messages, money) VALUES (%s, %s, %s, %s)"
        val = (ctx.member.id, 0, 0, 0, 0)
        c.execute(sql, val)
        con.commit()
        await buy_ext.app.rest.create_message(874675093354201148, hikari.Embed(
            title="Zarejestrowano nowego użytkownika",
            description=f"""Użytkownik <@{ctx.member.id}> ({ctx.member.id}) właśnie został zarejestrowany w bazie danych.
            
💾 **Wpisane dane:**
ID: `{ctx.member.id}`
XP: `0`
Level: `0`""", colour="#00ff00"))
        await ctx.respond(hikari.Embed(description="Nie byłeś/-aś wpisany do bazy danych. Już to zrobiłem 👴🏿!", colour="#ff0000"))
        return
        

def load(bot):
    bot.add_plugin(buy_ext)

def un_load(bot):
    bot.remove_plugin(buy_ext)
