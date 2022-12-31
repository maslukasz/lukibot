import hikari
import lightbulb
from unbelipy import UnbeliClient

partners_plugin = lightbulb.Plugin("Plugin stats_plugin")

client = UnbeliClient(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIxMDUxOTMwNDA2Mzg0OTYzMTk1IiwiaWF0IjoxNjcwODcwMTUyfQ.PQn4q5VPVLkiAqWQXhHRv3J8rljJPJjY4PNuE_IIrIQ")
guild_id = 630462196589264945

@partners_plugin.listener(hikari.GuildMessageCreateEvent)
async def leveling(event: hikari.Event) -> None:
    if event.author.is_bot or event.message.channel_id != 731952643437756467:
        return

    async with partners_plugin.bot.d.db.acquire() as con:
        c = await con.cursor()
    
    message = event.content
    
    if message.index('https://discord.gg/') or message.startswith('https://discord.gg/'):
        await c.execute(f"SELECT partnerships FROM userdata WHERE userid = {event.member.id}")
        r = await c.fetchone()
        await partners_plugin.bot.rest.create_message(731952643437756467, hikari.Embed(title="Nawiązano partnerstwo", description=f"""<@{event.author.id}> dziękujemy za nawiązanie partnerstwa! To Twoje **{int(r[0])+1}** partnerstwo. Otrzymujesz za to `{int(r[0])+1*1.2}` <:thend:742800976636936202>""", colour="#2F3136"))
        await c.execute(f"UPDATE userdata SET partnerships = {int(r[0])+1} WHERE userid = {event.member.id}")
        user_balance = await client.edit_user_balance(guild_id, event.member.id, cash=int(int(r[0])+1*2), reason="Partnerstwo")

    else:
        pass

def load(bot):
    bot.add_plugin(partners_plugin)

def unload(bot):
    bot.remove_plugin(partners_plugin)

