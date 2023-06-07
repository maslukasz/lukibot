import hikari
import lightbulb

unbe_plugin = lightbulb.Plugin("Slowka ")

@unbe_plugin.command()
@lightbulb.command("autoryzacja", "Link do autoryzacji bota w Unbelievableboat")
@lightbulb.implements(lightbulb.SlashCommand)
async def unbe_settings(ctx: lightbulb.Context) -> None:
    await ctx.respond(hikari.Embed(title="Dodaj autoryzację lukibota dla Twojego serwera!", description=f"""<:inv:797537658310098975> Zrobisz to pod adresem - https://unbelievaboat.com/applications/authorize?app_id=1051930406384963195. Dzięki temu bot będzie mógł edytować stan pieniężny użytkowników.""", colour="#00ff00"))

def load(bot):
    bot.add_plugin(unbe_plugin)

def unload(bot):
    bot.remove_plugin(unbe_plugin)
