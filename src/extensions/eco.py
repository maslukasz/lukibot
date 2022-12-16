import hikari
import lightbulb

import miru

config = lightbulb.Plugin("Ustawienia ekonomii - admin")

class ConfirmView(miru.View):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @miru.button(label="Tak", emoji=hikari.Emoji.parse('<:tak:866036793455280180>'), style=hikari.ButtonStyle.SUCCESS)
    async def confirm_button(self, button: miru.Button, ctx: miru.Context) -> None:
        async with config.bot.d.db.acquire() as con:
            c = await con.cursor()
        
        print(config.bot.d.testp)
        
        await c.execute(f"")
        await ctx.respond(hikari.Embed(title="Sukces!", description="<:tak:866036793455280180> Rola już nie będzie nadawana."))
@config.command()
@lightbulb.option("level", "Za osiągnięcie którego poziomu bot ma nadać rolę", type=hikari.OptionType.INTEGER)
@lightbulb.option("rola", "Rola, która będzie nadawana", type=hikari.Role)
@lightbulb.command("create-level-role", "Dodawanie roli za osiągnięcie danego poziomu")
@lightbulb.implements(lightbulb.SlashCommand)
async def leveling_roles_settings(ctx: lightbulb.Context) -> None:
    async with config.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT role FROM leveling_roles WHERE guild={str(ctx.get_guild().id)} AND role = {str(ctx.options.rola.id)}")
    r = c.fetchone()
    
    config.bot.d.test = ctx.options.rola

    if r is not None:
        view = ConfirmView()
        resp = await ctx.respond("Ta rola jest już zarejestrowana.", components=view.build())
        msg = await resp.message()

        view.start(msg)
        await view.wait()
    else:
        await c.execute(f"INSERT INTO leveling_roles (guild, role, level) VALUES ({str(ctx.get_guild().id)}, {str(ctx.options.rola.id)}, {str(ctx.options.level)}) WHERE guild = {str(ctx.get_guild().id)})")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz rola <@{ctx.options.rola.id}> będzie nadawana za **{ctx.options.level}** poziom!", colour="#00ff00"))



def load(bot):
    bot.add_plugin(config)

def unload(bot):
    bot.remove_plugin(config)
