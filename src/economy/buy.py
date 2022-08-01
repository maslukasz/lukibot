import hikari
import lightbulb

import random
import sqlite3

con = sqlite3.connect('main.db')
c = con.cursor()


buy_ext = lightbulb.Plugin("buy", "buy")

@buy_ext.command
@lightbulb.command('bal', 'buy command', aliases=['bala'])
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def bal(ctx: lightbulb.Context) -> None:
    c.execute(f'SELECT money FROM userdata WHERE userid = {ctx.member.id}')
    r = c.fetchone()
    await ctx.respond(r)

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

    if int(ctx.options.id) > 5 or int(ctx.options.id) == 0: # Aspołeczny
        await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Podano nieprawidłową wartość.', color='#ff0000'))
        return
    
    if int(ctx.options.id) == 1:
        if r[0] < 110000: # VIP
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 630485271221108766 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz zakupionego VIPa.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=630485271221108766)
            await ctx.respond(hikari.Embed(description="Zakupiono rolę <@&630485271221108766>! Korzyści tej roli znajdziesz [tutaj](https://discord.com/channels/630462196589264945/630462459458748417/827227351749230622) bądź klikając guziki w sklepie.", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-110000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 2: # Premium
        if r[0] < 150000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 630485155274031105 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz zakupionego VIPa.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=630485155274031105)
            await ctx.respond(hikari.Embed(description="Zakupiono rolę <@&630485155274031105>! Korzyści tej roli znajdziesz [tutaj](https://discord.com/channels/630462196589264945/630462459458748417/827227351749230622) bądź klikając guziki w sklepie.", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-150000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 3: # Supreme
        if r[0] < 250000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 688445563934474364 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz zakupionego VIPa.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=688445563934474364)
            await ctx.respond(hikari.Embed(description="Zakupiono rolę <@&688445563934474364>! Korzyści tej roli znajdziesz [tutaj](https://discord.com/channels/630462196589264945/630462459458748417/827227351749230622) bądź klikając guziki w sklepie.", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-250000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 4: # Bogacz
        if r[0] < 500000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 698989932772851715 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz zakupionego VIPa.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=698989932772851715)
            await ctx.respond(hikari.Embed(description="Zakupiono rolę <@&698989932772851715>! Korzyści tej roli znajdziesz [tutaj](https://discord.com/channels/630462196589264945/630462459458748417/827227351749230622) bądź klikając guziki w sklepie.", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-500000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 5: # Szejk
        if r[0] < 1000000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 698989933188350082 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz zakupionego VIPa.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=698989933188350082)
            await ctx.respond(hikari.Embed(description="Zakupiono rolę <@&698989933188350082>! Korzyści tej roli znajdziesz [tutaj](https://discord.com/channels/630462196589264945/630462459458748417/827227351749230622) bądź klikając guziki w sklepie.", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-1000000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

@buy.child
@lightbulb.option('id', 'item id')
@lightbulb.command('uslugi', 'premium subcommand', aliases=['usługi'])
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def uslugi(ctx: lightbulb.Context) -> None:
    c.execute(f'SELECT money FROM userdata WHERE userid = {ctx.member.id}')
    r = c.fetchone()

    if int(ctx.options.id) > 1 or int(ctx.options.id) == 0: # Aspołeczny
        await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Podano nieprawidłową wartość.', color='#ff0000'))
        return

    if int(ctx.options.id) == 1: # ticket ogłoszeń
        if r[0] < 90000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 688712947299647499 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz zakupiony ticket ogłoszeń.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=688712947299647499)
            await ctx.respond(hikari.Embed(description="Zakupiono <@&688712947299647499>! Teraz masz możliwość wysłania jednego ogłoszenia na <#737431057686593597>.", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-90000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

@buy.child
@lightbulb.option('id', 'item id')
@lightbulb.command('kolory', 'premium subcommand', aliases=['kolor'])
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def kolory(ctx: lightbulb.Context) -> None:
    c.execute(f'SELECT money FROM userdata WHERE userid = {ctx.member.id}')
    r = c.fetchone()

    if int(ctx.options.id) > 20 or int(ctx.options.id) == 0: # Aspołeczny
        await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Podano nieprawidłową wartość.', color='#ff0000'))
        return

    teksty = ['Ładnie Ci z nim :blush:', 'Epicko teraz będziesz wyglądał/-a 😈', 'Oby Ci pasował, bo niezła fortunka na niego poszła 😳', 'O wiele piękniejszy/-a teraz jesteś...', 'Ten co teraz miałeś/-aś był fatalny. Dobra zmiana', 'Niby spoko ten kolorek, ale można było ten hajs dać do skarbu serwera 🙄 Żartowałem 👴🏿']
    random_teksty = random.choice(teksty)
    if int(ctx.options.id) == 1:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 690245468365652012 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=690245468365652012)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&690245468365652012>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()
    
    if int(ctx.options.id) == 2:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 689662720039059546 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=689662720039059546)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&689662720039059546>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()
            
    if int(ctx.options.id) == 3:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 688134141190996001 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=688134141190996001)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&688134141190996001>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 4:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 688133947632123974 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=688133947632123974)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&688133947632123974>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 5:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 688134526106730578 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=688134526106730578)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&688134526106730578>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 6:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 717038563593551884 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=717038563593551884)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&717038563593551884>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 7:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 716915038153080864 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=716915038153080864)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&716915038153080864>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 8:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 717038568366669986 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=717038568366669986)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&717038568366669986>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 9:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 716915036634742884 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=716915036634742884)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&716915036634742884>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 10:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 717038565372198952 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=717038565372198952)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&717038565372198952>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 11:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 690245469187997747 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=690245469187997747)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&690245469187997747>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 12:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 688134619731722240 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=688134619731722240)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&688134619731722240>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 13:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 688134252440846391 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=688134252440846391)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&688134252440846391>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 14:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 689662738133417992 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=689662738133417992)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&689662738133417992>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 15:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 688134445332561955 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=688134445332561955)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&688134445332561955>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 16:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 716915038916444211 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=716915038916444211)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&716915038916444211>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 17:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 717038566818971769 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=717038566818971769)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&717038566818971769>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 18:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 717038561505050694 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=717038561505050694)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&717038561505050694>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 19:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 717038559537660066 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=717038559537660066)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&717038559537660066>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 20:
        if r[0] < 100000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 688133448770387989 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz ten kolor.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=688133448770387989)
            await ctx.respond(hikari.Embed(description=f"Zakupiono kolor <@&688133448770387989>! {random_teksty}", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-100000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

@buy.child
@lightbulb.option('id', 'item id')
@lightbulb.command('dodatki', 'premium subcommand')
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def dodadtki(ctx: lightbulb.Context) -> None:
    c.execute(f'SELECT money FROM userdata WHERE userid = {ctx.member.id}')
    r = c.fetchone()

    if int(ctx.options.id) > 4 or int(ctx.options.id) == 0: # Aspołeczny
        await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Podano nieprawidłową wartość.', color='#ff0000'))
        return
    
    if int(ctx.options.id) == 1: # Aspołeczny
        if r[0] < 80000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 727190590000857121 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz zakupiony ticket ogłoszeń.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=727190590000857121)
            await ctx.respond(hikari.Embed(description="Zakupiono dodatkową rolę <@&727190590000857121>! Możesz czuć się wyróżniony/-a na tle innych ;)", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-80000, ctx.author.id)
            c.execute(sql, val)
            con.commit()
    
    if int(ctx.options.id) == 2: # haker
        if r[0] < 80000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 727190590873141251 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz zakupiony ticket ogłoszeń.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=727190590873141251)
            await ctx.respond(hikari.Embed(description="Zakupiono dodatkową rolę <@&727190590873141251>! Możesz czuć się wyróżniony/-a na tle innych ;)", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-80000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 3: # marzyciel
        if r[0] < 80000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 727190592400130090 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz zakupiony ticket ogłoszeń.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=727190592400130090)
            await ctx.respond(hikari.Embed(description="Zakupiono dodatkową rolę <@&727190592400130090>! Możesz czuć się wyróżniony/-a na tle innych ;)", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-80000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

    if int(ctx.options.id) == 4: # wszechwiedzący
        if r[0] < 80000:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Nie masz tyle na koncie', color='#ff0000'))
            return
        if 727190588650291220 in ctx.member.role_ids:
            await ctx.respond(hikari.Embed(description='<:nie:783659534455275560> Już masz zakupiony ticket ogłoszeń.', color='#ff0000'))
            return
        else:
            await buy_ext.app.rest.add_role_to_member(user=ctx.member.id, guild=ctx.guild_id, role=727190588650291220)
            await ctx.respond(hikari.Embed(description="Zakupiono dodatkową rolę <@&727190588650291220>! Możesz czuć się wyróżniony/-a na tle innych ;)", color='#00ff00'))
            sql = "UPDATE userdata SET money = ? WHERE userID = ?"
            val = (r[0]-80000, ctx.author.id)
            c.execute(sql, val)
            con.commit()

def load(bot):
    bot.add_plugin(buy_ext)

def un_load(bot):
    bot.remove_plugin(buy_ext)
