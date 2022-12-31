import hikari
import lightbulb

unbe_plugin = lightbulb.Plugin("Slowka ")

@unbe_plugin.command()
@lightbulb.option("token", "Token aplikacji Unbelievableboat", required=True, type=str)
@lightbulb.command("unbelievable_config", "Ustawienie tokenu aplikacji Unbelievableboat do poprawnego działania rozszerzenia")
@lightbulb.implements(lightbulb.SlashCommand)
async def unbe_settings(ctx: lightbulb.Context) -> None:
    async with unbe_plugin.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT token FROM unbe_settings WHERE guild = {ctx.get_guild().id}")


def load(bot):
    bot.add_plugin(unbe_plugin)

def unload(bot):
    bot.remove_plugin(unbe_plugin)
