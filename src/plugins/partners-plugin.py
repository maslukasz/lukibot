import hikari
import lightbulb

import psycopg2

partners_plugin = lightbulb.Plugin("Plugin stats_plugin")

con = psycopg2.connect(
        host="localhost",
        dbname="demo",
        user='postgres',
        password='admin',
        port=5432)
    
c = con.cursor()


@partners_plugin.listener(hikari.GuildMessageCreateEvent)
async def leveling(event: hikari.Event) -> None:
    if event.author.is_bot or event.message.channel_id != 731952643437756467:
        return

    message = event.content
    
    if message.index('https://discord.gg/'):
        c.execute(f"SELECT partnerships FROM userdata WHERE userid = {event.member.id}")
        r = c.fetchone()
        partners = int(r[0])
        new_partners = partners + 1
        c.execute(f"UPDATE userdata SET partnerships = {new_partners} WHERE userid = {event.member.id}")
        con.commit()



def load(bot):
    bot.add_plugin(partners_plugin)

def unload(bot):
    bot.remove_plugin(partners_plugin)

