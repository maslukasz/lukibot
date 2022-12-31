import hikari
import lightbulb
import miru

import datetime

user_extension = lightbulb.Plugin("Rawki", "Plugin z gotowymi komendami")

class ProfilView(miru.View):
    @miru.button(label=" ", emoji='🏠', style=hikari.ButtonStyle.SUCCESS)
    async def home_button(self, button: miru.Button, ctx: miru.Context) -> None:
        async with user_extension.bot.d.db.acquire() as con:
            c = await con.cursor()

        await c.execute(f"SELECT xp, level, money, about FROM userdata WHERE userid = {ctx.member.id}")
        r = await c.fetchone()

        await ctx.edit_response(hikari.Embed(title=f'Strona główna',
        description=f"""<:kropka:756964971300257814> **Stan konta**: `{r[2]}` <:thend:742800976636936202>
<:kropka:756964971300257814> **Poziom**: `{r[1]}` (`{r[0]}` XP)

Opis:
{r[3]}""", colour='4F545C'))

    @miru.button(label=" ", emoji='📊', style=hikari.ButtonStyle.SECONDARY)
    async def statystyki_button(self, button: miru.Button, ctx: miru.Context) -> None:
        async with user_extension.bot.d.db.acquire() as con:
            c = await con.cursor()
            c2 = await con.cursor()
            c3 = await con.cursor()
            c4 = await con.cursor()
            c5 = await con.cursor()

        # Łączna ilość wiadomości
        await c.execute(f"SELECT SUM(messages) FROM history_users WHERE userid = {ctx.member.id}")
        r = await c.fetchone()
        
        # Wiadomości z ostatnich 7 dni
        await c2.execute(f"SELECT SUM(messages) FROM history_users WHERE userid = {ctx.member.id} AND data BETWEEN DATE_ADD(now(), INTERVAL -7 day) AND date(now())")
        r2 = await c2.fetchone()

        await c3.execute(f"SELECT channel, SUM(messages) FROM history_users WHERE userid = {ctx.member.id} GROUP BY channel ORDER BY sum(messages) DESC")

        r3 = await c3.fetchall()
        print(r3)
        
        await c4.execute(f"SELECT SUM(messages), channel, data FROM history_users WHERE userid = {ctx.member.id} GROUP BY channel ORDER BY messages DESC")
        r4 = await c4.fetchall()

        await c5.execute(f'SELECT data, messages FROM history_users WHERE userid = {ctx.member.id} GROUP BY data ORDER BY messages DESC')
        r5 = await c5.fetchone()
        top7 = " "

        print(r2)

        if len(r3) < 3:
            top7 = "Nie napisałeś/-aś jescze wiadomości na przynajmniej 3 kanałach"
        else:
            top7 = f"""<:kropka:756964971300257814> <#{r3[0][0]}> **{r3[0][1]}** wiadomości
<:blurpledot:925702134467551273> <#{r3[1][0]}> **{r3[1][1]}** wiadomości
<:blurpledot:925702134467551273> <#{r3[2][0]}> **{r3[2][1]}** wiadomości"""

        await ctx.edit_response(hikari.Embed(title=f'Statystyki {ctx.member}',
        description=f"""🏅 **Serwerowe**
<:kropka:756964971300257814> Tytuły Użytkownika Tygodnia: `brak`.
<:kropka:756964971300257814> Tytuły Użytkownika Miesiąca: `brak`.
~~<:kropka:756964971300257814> Wykonane questy: `brak`.~~ Questy nie są jeszcze dodane do bota.
<:kropka:756964971300257814> Wykonane partnerstwa: `brak`.

💬 **Twoje TOP 3 kanały**
{top7}

📂 **Dodatkowe**
<:kropka:756964971300257814> Łącznie napisane wiadomości: `{r[0]}`
~~<:kropka:756964971300257814> Dzień, w którym napisano najwięcej wiadomości: `{r5[0]}` (**{r5[0][0]}** wiadomości)~~ Do naprawienia
<:kropka:756964971300257814> Wiadomości przez ostatnie 7 dni: `{r2[0]}`
<:kropka:756964971300257814> Najbardziej aktywny kanał: <#{r4[0][1]}> (`{r4[0][0]}` wiadomości)
<:kropka:756964971300257814> Na ilu łącznie kanałach została wysłana przynajmniej 1 wiadomość: `{len(r3)}`""".replace('None', "Wystąpił błąd z Twoimi danymi. Albo za mało tu pisałeś/-aś, albo coś się wywaliło. Jeśli błąd będzie się powtarzał, to napisz do administracji."), colour='4F545C'))

    @miru.button(label=" ", emoji='🕥', style=hikari.ButtonStyle.DANGER)
    async def cooldowns_button(self, button: miru.Button, ctx: miru.Context) -> None:
        async with user_extension.bot.d.db.acquire() as con:
            c = await con.cursor()

        await c.execute(f"""SELECT work, CASE
        WHEN work IS NOT NULL THEN unix_timestamp(work)
        END FROM cooldowns WHERE userid = {ctx.member.id}""")
        r = await c.fetchone()

        if r is None:
            work = "<:tak:866036793455280180> `;work`: **Brak cooldownu**"
        elif r[0] < str(datetime.datetime.now()):
            work = f"<:tak:866036793455280180> `;work`: **Brak cooldownu**. Ostatnie użycie było <t:{int(r[1])}:R>"
        else:
            work = f"<:nie:866036882553700353> `;work`: <t:{int(r[1])}:R>"

        await ctx.edit_response(hikari.Embed(title=f'Cooldowny',
        description=f"""{work}""", colour='4F545C'))

@user_extension.command
@lightbulb.command("profil", "Wyświetl swoje dane", aliases=['prof', 'profile'])
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def profil(ctx: lightbulb.Context) -> None:
    async with user_extension.bot.d.db.acquire() as con:
            c = await con.cursor()

    await c.execute(f"SELECT xp, level, money, about FROM userdata WHERE userid = {ctx.author.id}")
    r = await c.fetchone()
    lvl_end = int(r[0] ** (1 / 4))

    view = ProfilView()
    resp = await ctx.respond(hikari.Embed(title=f'Strona główna',
    description=f"""<:kropka:756964971300257814> **Stan konta**: `{r[2]}` <:thend:742800976636936202>
<:kropka:756964971300257814> **Poziom**: `{r[1]}` (**{r[0]}**/{lvl_end} XP)

Opis:
{r[3]}""", colour='#4F545C'), components=view.build())
    message = await resp.message()
    await view.start(message)
    await view.wait()
        

def load(bot):
    bot.add_plugin(user_extension)

def unload(bot):
    bot.remove_plugin(user_extension)
