import hikari, lightbulb
from lightbulb.ext import tasks

admin_extension = lightbulb.Plugin("asklda")

@admin_extension.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("channel", "Kanał, który ma być ignorowany w naliczaniu statystyk i xp.", type=hikari.TextableGuildChannel)
@lightbulb.command("config-ignored-add", 'asdasdasd sdadaasd')
@lightbulb.implements(lightbulb.SlashCommand)
async def config_ignored_add(ctx: lightbulb.Context):
    async with admin_extension.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT ignored FROM channels WHERE guild_id={ctx.get_guild().id} AND ignored = {ctx.options.channel.id}")
    r = await c.fetchone()
    print(r)
    print(ctx.options.channel.id)

    if r is None:
        await c.execute(f"INSERT INTO channels (guild_id, ignored) VALUES ({ctx.get_guild().id}, {ctx.options.channel.id})")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz kanał <#{ctx.options.channel.id}> będzie ignorowany!", colour="#00ff00"))
    else:
        await ctx.respond(hikari.Embed(title="Coś poszło nie tak!",
        description=f"""<:nie:866036882553700353> Podany kanał jest już ignorowany.""", color='#ff0000'))

@admin_extension.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("channel", "Usuwanie kanału z listy ignorowanych.", type=hikari.TextableGuildChannel)
@lightbulb.command("config-ignored-remove", 'Usuwanie kanału z ignorowanych')
@lightbulb.implements(lightbulb.SlashCommand)
async def config_ignored_add(ctx: lightbulb.Context):
    async with admin_extension.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT ignored FROM channels WHERE guild_id={ctx.get_guild().id} AND ignored = {ctx.options.channel.id}")
    r = await c.fetchone()
    print(r)
    print(ctx.options.channel.id)

    if r is not None:
        await c.execute(f"DELETE FROM channels WHERE guild_id = {ctx.get_guild().id} AND ignored = {ctx.options.channel.id}")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz kanał <#{ctx.options.channel.id}> nie będzie ignorowany!", colour="#00ff00"))
    else:
        await ctx.respond(hikari.Embed(title="Coś poszło nie tak!",
        description=f"""<:nie:866036882553700353> Podany kanał nie był ignorowany.""", color='#ff0000'))

@admin_extension.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("channel", "Kanał, na którym bot będzie automatycznie zliczał partnerstwa użytkownikom.", type=hikari.TextableGuildChannel)
@lightbulb.command("config-partnerships-set", 'Kanał partnerstw.')
@lightbulb.implements(lightbulb.SlashCommand)
async def config_partnerships_set(ctx: lightbulb.Context):
    async with admin_extension.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT partnerships_channel, guild_id FROM config_values WHERE guild_id={ctx.get_guild().id}")
    r = await c.fetchone()
    print(r)
    print(ctx.options.channel.id)

    if r is None:
        await c.execute(f"INSERT INTO config_values (guild_id, partnerships_channel) VALUES ({ctx.get_guild().id}, {ctx.options.channel.id})")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz kanał <#{ctx.options.channel.id}> będzie kanałem od partnerstw.", colour="#00ff00"))
    if r == '0':
        await c.execute(f"UPDATE config_values SET partnerships_channel = {ctx.options.channel.id} WHERE guild_id = {ctx.get_guild().id}")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz kanał <#{ctx.options.channel.id}> będzie kanałem od partnerstw.", colour="#00ff00"))
    elif r[0] == str(ctx.options.channel.id):
        await ctx.respond(hikari.Embed(title="Coś poszło nie tak!",
        description=f"""<:nie:866036882553700353> Ten kanał jest już ustawiony jako kanał partnerstw.""", color='#ff0000'))
    else:
        await c.execute(f"UPDATE config_values SET partnerships_channel = {ctx.options.channel.id} WHERE guild_id = {ctx.get_guild().id}")
        await ctx.respond(hikari.Embed(title="Uwaga!",
        description=f"""<:neutral:866036839348699176> Kanał został zmieniony z <#{r[0]}> na <#{ctx.options.channel.id}>.""", color='#ffa500'))

@admin_extension.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.command("toggle-xp-mode", 'Przełącz tryb XP (on/off)')
@lightbulb.implements(lightbulb.SlashCommand)
async def toggle_xp(ctx: lightbulb.Context):
    async with admin_extension.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT xp_system FROM config_values WHERE guild_id={ctx.get_guild().id}")
    r = await c.fetchone()
    print(r)

    if r is None:
        await c.execute(f"INSERT INTO config_values(guild_id, xp_system) VALUES ({ctx.get_guild().id}, False)")
        await ctx.respond(hikari.Embed(title="Coś poszło nie tak!",
        description=f"""<:nie:866036882553700353> Twój serwer nie był zarejestrowany w bazie (nie wiem jak to możliwe XD), ale już to zmieniłem. Użyj komendy jeszcze raz.""", color='#ff0000'))
    
    if r[0] == 1:
        await c.execute(f"UPDATE config_values SET xp_system = 0 WHERE guild_id = {ctx.get_guild().id}")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:switchno:785979057736777728> Od teraz system XP jest wyłączony!", colour="#72767C"))
    else:
        await c.execute(f"UPDATE config_values SET xp_system = 1 WHERE guild_id = {ctx.get_guild().id}")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:switchyes:785978769848270889> Od teraz system XP jest włączony!", colour="#00ff00"))


@admin_extension.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("channel", "Kanał logów lukibota", type=hikari.TextableGuildChannel)
@lightbulb.command("log-channel-set", 'Kanał logów')
@lightbulb.implements(lightbulb.SlashCommand)
async def config_partnerships_set(ctx: lightbulb.Context):
    async with admin_extension.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT log_channel, guild_id FROM config_values WHERE guild_id={ctx.get_guild().id}")
    r = await c.fetchone()

    if r is None:
        await c.execute(f"INSERT INTO config_values (guild_id, log_channel) VALUES ({ctx.get_guild().id}, {ctx.options.channel.id})")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz kanał <#{ctx.options.channel.id}> będzie kanałem od logów.", colour="#00ff00"))
    elif r [0] == '0':
        await c.execute(f"UPDATE config_values SET log_channel = {ctx.options.channel.id} WHERE guild_id = {ctx.get_guild().id}")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz kanał <#{ctx.options.channel.id}> będzie kanałem od logów.", colour="#00ff00"))
    elif r[0] == str(ctx.options.channel.id):
        await ctx.respond(hikari.Embed(title="Coś poszło nie tak!",
        description=f"""<:nie:866036882553700353> Ten kanał jest już ustawiony jako kanał logów.""", color='#ff0000'))
    else:
        await c.execute(f"UPDATE config_values SET log_channel = {ctx.options.channel.id} WHERE guild_id = {ctx.get_guild().id}")
        await ctx.respond(hikari.Embed(title="Uwaga!",
        description=f"""<:neutral:866036839348699176> Kanał został zmieniony z <#{r[0]}> na <#{ctx.options.channel.id}>.""", color='#ffa500'))

@admin_extension.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("channel", "Usuwanie kanału logów.", type=hikari.TextableGuildChannel)
@lightbulb.command("log-channel-remove", 'Usuwanie kanału logów.')
@lightbulb.implements(lightbulb.SlashCommand)
async def config_ignored_add(ctx: lightbulb.Context):
    async with admin_extension.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT log_channel FROM config_values WHERE guild_id={ctx.get_guild().id} AND log_channel = {ctx.options.channel.id}")
    r = await c.fetchone()

    if r is not None:
        await c.execute(f"DELETE FROM channels log_channel WHERE guild_id = {ctx.get_guild().id} AND log_channel = {ctx.options.channel.id}")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz kanał <#{ctx.options.channel.id}> nie kanałem logów!", colour="#00ff00"))
    else:
        await ctx.respond(hikari.Embed(title="Coś poszło nie tak!",
        description=f"""<:nie:866036882553700353> Nigdy nie ustawiono kanału logów.""", color='#ff0000'))


@admin_extension.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("role", "Rola, która ma być automatycznie nadawana partnerom", type=hikari.Role)
@lightbulb.command("config-partnerships-role", 'Ustawianie roli partnerów')
@lightbulb.implements(lightbulb.SlashCommand)
async def config_partnerships_set(ctx: lightbulb.Context):
    async with admin_extension.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f"SELECT partnership_rank, guild_id FROM config_values WHERE guild_id={ctx.get_guild().id}")
    r = await c.fetchone()
    print(r)

    
    if r is None:
        await c.execute(f"INSERT INTO config_values (guild_id, partnership_rank) VALUES ({ctx.get_guild().id}, {ctx.options.role.id})")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz rola <@&{ctx.options.role.id}> będzie nadawana partnerom.", colour="#00ff00"))
        return
    if r[0] == '0':
        await c.execute(f"UPDATE config_values SET partnership_rank = {ctx.options.role.id} WHERE guild_id = {ctx.get_guild().id}")
        await ctx.respond(hikari.Embed(title="Sukces!", description=f"<:tak:866036793455280180> Od teraz rola <@&{ctx.options.role.id}> będzie nadawana partnerom.", colour="#00ff00"))
    elif r[0] == str(ctx.options.role.id):
        await ctx.respond(hikari.Embed(title="Coś poszło nie tak!",
        description=f"""<:nie:866036882553700353> Ta rola jest już ustawiona jako rola partnerów.""", color='#ff0000'))
    else:
        await c.execute(f"UPDATE config_values SET partnership_rank = {ctx.options.role.id} WHERE guild_id = {ctx.get_guild().id}")
        await ctx.respond(hikari.Embed(title="Uwaga!",
        description=f"""<:neutral:866036839348699176> Rola partnerów została zmieniona z <@&{r[0]}> na <#{ctx.options.role.id}>.""", color='#ffa500'))


def load(bot):
    bot.add_plugin(admin_extension)

def unload(bot):
    bot.remove_plugin(admin_extension)