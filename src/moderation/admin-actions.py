import hikari, lightbulb

admin_extension = lightbulb.Plugin("asklda")

@admin_extension.command
@lightbulb.command("ban", 'asdasdasd sdadaasd')
@lightbulb.implements(lightbulb.PrefixCommand)
async def asdkkdss(ctx: lightbulb.Context):
    async with admin_extension.bot.d.db.acquire() as con:
        c = await con.cursor()
        c2 = await con.cursor()

    await c.execute(f"SELECT role, level FROM leveling_roles WHERE guild={str(ctx.get_guild().id)}")
    r = await c.fetchall()

    for role in r:

        print(role)
        ctx.respond(role)

def load(bot):
    bot.add_plugin(admin_extension)

def unload(bot):
    bot.remove_plugin(admin_extension)