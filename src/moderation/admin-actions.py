import hikari, lightbulb

admin_extension = lightbulb.Plugin("asklda")

@admin_extension.command
@lightbulb.add_checks(lightbulb.has_roles(790937105214734360))
@lightbulb.command("ban", 'asdasdasd sdadaasd')
@lightbulb.implements(lightbulb.PrefixCommand)
async def asdkkdss(ctx: lightbulb.Context):
    await ctx.respond("test")

def load(bot):
    bot.add_plugin(admin_extension)

def unload(bot):
    bot.remove_plugin(admin_extension)