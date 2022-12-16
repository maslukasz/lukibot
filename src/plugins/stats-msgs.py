import hikari
import lightbulb
from unbelipy import UnbeliClient

import requests

client = UnbeliClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIxMDUxOTMwNDA2Mzg0OTYzMTk1IiwiaWF0IjoxNjcwODcwMTUyfQ.PQn4q5VPVLkiAqWQXhHRv3J8rljJPJjY4PNuE_IIrIQ")
guild_id = 630462196589264945


stats_plugin = lightbulb.Plugin("Plugin stats_plugin")


@stats_plugin.listener(hikari.GuildMessageCreateEvent)
async def leveling(event: hikari.Event) -> None:
    if event.author.is_bot:
        return
    
    async with stats_plugin.bot.d.db.acquire() as con:
        c = await con.cursor()
    
    print("a")

    await c.execute(f"SELECT messages, channel, data FROM history_users WHERE userid = {str(event.author.id)} AND channel = {str(event.message.channel_id)} AND data = date(now())")
    r = await c.fetchone()

    if r is None:
        await c.execute(f"INSERT INTO history_users(userid, channel, data, messages) VALUES ({str(event.author.id)}, {str(event.message.channel_id)}, date(now()), 1)")
        await stats_plugin.bot.rest.create_message(874675093354201148, hikari.Embed(title="Zmiana w bazie danych", description=f"""Kanał <#{event.message.channel_id}> został zarejestrowany w `history_users` dla <@{event.author.id}>""", colour="#00FF00"))
        return

    await c.execute(f"UPDATE history_users SET messages = {int(r[0])+1} WHERE userid = {str(event.author.id)} AND channel = {str(event.message.channel_id)} AND data = date(now())")


def load(bot):
    bot.add_plugin(stats_plugin)

def unload(bot):
    bot.remove_plugin(stats_plugin)

