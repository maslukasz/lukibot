import hikari
import lightbulb


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




def load(bot):
    bot.add_plugin(help_plugin)

def unload(bot):
    bot.remove_plugin(help_plugin)

