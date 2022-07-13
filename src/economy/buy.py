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
async def buy(ctx: lightbulb.Context) -> None:
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

    await ctx.respond(hikari.Embed(title="Nie podano argumentów",
    description="""Aby coś kupić, musisz użyć komendy `buy` (lub `kup`). Poprawne użycie tej komendy to `,kup <kategoria> <ID przedmiotu>`.""", colour='#FF0000'))

@buy.child
@lightbulb.option('id', 'item id')
@lightbulb.command('premium', 'premium subcommand')
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def premium(ctx: lightbulb.Context) -> None:
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

    if int(ctx.options.id) == 1:
        if r[0] < 110000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        else:
            if 630485271221108766 in ctx.member.role_ids:
                await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz zakupionego VIPa.', color='#ff0000'))
                return
            else:
                money = int(r[0]-110000)
                sql = ("UPDATE userdata SET money = %s WHERE userid = %s")
                val = (money, ctx.member.id)
                c.execute(sql, val)
                con.commit()
                await ctx.bot.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=630485271221108766)
                await ctx.respond(hikari.Embed(description="Zakupiono VIPa.", color='#00ff00'))

def load(bot):
    bot.add_plugin(buy_ext)

def un_load(bot):
    bot.remove_plugin(buy_ext)
