import hikari
import lightbulb




stats_plugin = lightbulb.Plugin("Plugin stats_plugin")


@stats_plugin.listener(hikari.GuildMessageCreateEvent)
async def leveling(event: hikari.Event) -> None:
    if event.author.is_bot:
        return
    
    async with stats_plugin.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f'SELECT * from channels WHERE guild_id = {event.get_guild().id}')
    ignored_channels = await c.fetchone()

    if ignored_channels is not None and str(event.get_channel().id) in ignored_channels:
        return

    await c.execute(f"SELECT messages, channel, data FROM history_users WHERE user_id = {str(event.author.id)} AND guild_id = {event.get_guild().id} AND channel = {str(event.message.channel_id)} AND data = date(now())")
    r = await c.fetchone()

    if r is None:
        await c.execute(f"INSERT INTO history_users(guild_id, user_id, channel, data, messages) VALUES ({event.get_guild().id}, {str(event.author.id)}, {str(event.message.channel_id)}, date(now()), 1)")
        #await stats_plugin.bot.rest.create_message(874675093354201148, hikari.Embed(title="Zmiana w bazie danych", description=f"""Kanał <#{event.message.channel_id}> został zarejestrowany w `history_users` dla <@{event.author.id}>""", colour="#00FF00"))
        return

    await c.execute(f"UPDATE history_users SET messages = {int(r[0])+1} WHERE user_id = {str(event.author.id)} AND guild_id = {event.get_guild().id} AND channel = {str(event.message.channel_id)} AND data = date(now())")


def load(bot):
    bot.add_plugin(stats_plugin)

def unload(bot):
    bot.remove_plugin(stats_plugin)

