import hikari
import lightbulb

import requests


help_plugin = lightbulb.Plugin("Plugin stats_plugin")


@help_plugin.command 
@lightbulb.command("help", 'help', aliases='pomoc')
@lightbulb.implements(lightbulb.PrefixCommand)
async def help(ctx: lightbulb.Context) -> None:
    await ctx.respond(hikari.Embed(title="Centrum pomocy",
    description=f"""Witaj <@{ctx.author.id}>, mój prefix to `;`. Tutaj przedstawię Ci najważniejsze komendy. Jeśli coś będzie niejasne, to skontaktuj się z administracją na <#688509218164047880>
    
**Ogólne**
```profil```
**Ekonomia**
```work, sklep, kup```
**Spisowe**
```rekordy```"""))


@help_plugin.command 
@lightbulb.command("askai", 'askai', aliases='ai')
@lightbulb.implements(lightbulb.PrefixCommand)
async def help(ctx: lightbulb.Context) -> None:
    async with help_plugin.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute("SELECT ad, user_id FROM partners ORDER BY RAND() LIMIT 1")
    r = await c.fetchone()

    text = str(r[0])


    await ctx.respond(text.replace(f"<@{r[1]}>", " "))

def load(bot):
    bot.add_plugin(help_plugin)

def unload(bot):
    bot.remove_plugin(help_plugin)

