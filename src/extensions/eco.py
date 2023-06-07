import hikari
import lightbulb

import miru

config = lightbulb.Plugin("Ustawienia ekonomii - admin")

# @config.command()
# @lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
# @lightbulb.option("level", "Za osiągnięcie którego poziomu bot ma nadać rolę", type=hikari.OptionType.INTEGER)
# @lightbulb.option("rola", "Rola, która będzie nadawana", type=hikari.Role)
# @lightbulb.command("create-level-role", "Dodawanie roli za osiągnięcie danego poziomu")
# @lightbulb.implements(lightbulb.SlashCommand)
# async def leveling_roles_settings(ctx: lightbulb.Context) -> None:
#     async with config.bot.d.db.acquire() as con:
#         c = await con.cursor()
#         c2 = await con.cursor()

#     await c.execute(f"SELECT role, level FROM leveling_roles WHERE guild={str(ctx.get_guild().id)} AND role = {str(ctx.options.rola.id)} OR level = {str(ctx.options.level)}")
#     r = await c.fetchone()

#     if r is not None:
#         await ctx.respond(hikari.Embed(title="Coś poszło nie tak!",
#         description=f"""<:nie:866036882553700353> Znaleziono duplikat w bazie danych. Poniżej masz zapis, w którym znaleziono powtórzone dane:
# ```ID roli: {r[0]}
# Level: {r[1]}```
# Dane, które wprowadzasz:
# ```ID roli: {ctx.options.rola.id}
# Level: {ctx.options.level}```
# Pamiętaj, że ani rola, ani level **nie** mogą się powtarzać.""", color='#ff0000'))
#     else:
#         await c.execute(f"INSERT INTO leveling_roles (guild, role, level) VALUES ({str(ctx.get_guild().id)}, {str(ctx.options.rola.id)}, {str(ctx.options.level)})")
#         await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz rola <@&{ctx.options.rola.id}> będzie nadawana za **{ctx.options.level}** poziom!", colour="#00ff00"))

# @config.command
# @lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
# @lightbulb.option("level", "Rola za który poziom ma zostać usunięta")
# @lightbulb.command("remove-level-role", "Usunięcie roli za osięgnięcie konkretnego poziomu")
# @lightbulb.implements(lightbulb.SlashCommand)
# async def leveling_roles_remove(ctx: lightbulb.Context) -> None:
#     async with config.bot.d.db.acquire() as con:
#         c = await con.cursor()

#     await c.execute(f"SELECT role FROM leveling_roles WHERE guild={str(ctx.get_guild().id)} AND level = {str(ctx.options.level)}")
#     r = await c.fetchone()

#     if r is None:
#         await ctx.respond(hikari.Embed(title="Coś poszło nie tak!",
#         description=f"""<:nie:866036882553700353> Nie ustawiono żadnej roli do nadawania za `{ctx.options.level}` poziom.""", color='#ff0000'))
#     else:
#         await c.execute(f"DELETE FROM leveling_roles WHERE level = {ctx.options.level} AND guild = {ctx.get_guild().id}")
#         await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz rola <@&{r[0]}>, która była za **{ctx.options.level}** poziom nie będzie nadawana!", colour="#00ff00"))

def load(bot):
    bot.add_plugin(config)

def unload(bot):
    bot.remove_plugin(config)
