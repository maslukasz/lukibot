import hikari
import lightbulb

partners_plugin = lightbulb.Plugin("Plugin stats_plugin")


@partners_plugin.listener(hikari.GuildMessageCreateEvent)
async def leveling(event: hikari.Event) -> None:
    if event.author.is_bot:
        return

    async with partners_plugin.bot.d.db.acquire() as con:
        c = await con.cursor()
        c2 = await con.cursor()
        c3 = await con.cursor()

    await c.execute(f"SELECT partnerships_channel FROM config_values WHERE guild_id = {event.get_guild().id}")
    r = await c.fetchone()

    if r is None:
        return

    if str(event.message.channel_id) not in r:
        return
    
    message = event.content
    if message.index('https://discord.gg/') or message.startswith('https://discord.gg/'):
        await c2.execute(f"SELECT partnerships FROM userdata WHERE user_id = {event.member.id} AND guild_id = {event.get_guild().id}")
        r2 = await c2.fetchone()

        await c3.execute(f'SELECT partnership_earning, partnership_multiplier, partnership_rank FROM config_values WHERE guild_id = {event.get_guild().id}')
        r3 = await c3.fetchone()
        msg_link = f'https://discord.com/channels/{event.get_guild().id}/{event.get_channel().id}/{event.message.id}'

        partner_msg = "\n\n<:nie:866036882553700353> Nie oznaczono partnera w reklamie."

        print(event.message.user_mentions_ids)

        if event.message.user_mentions_ids != []:
            print("asd")
            await c.execute(f"INSERT INTO partners (guild_id, user_id, ad_link, ad) VALUES({event.get_guild().id}, {event.message.user_mentions_ids[0]}, '{msg_link}', '{message}')")
            if r3[2] != '0':
                await partners_plugin.bot.rest.add_role_to_member(guild=event.get_guild().id, user=event.message.user_mentions_ids[0], role=int(r3[2]))
                partner_msg = f"\n\n<:TE_Partner:1111739353367068774> Partnerstwo nawiązane z <@{event.message.user_mentions_ids[0]}> i partner otrzymał rolę."
            else:
                partner_msg = f"\n\n<:TE_Partner:1111739353367068774> Partnerstwo nawiązane z <@{event.message.user_mentions_ids[0]}>\n<:TE_Warning:1111741159186907317> **Nie ustawiono roli partnerów**"

        await c2.execute(f"UPDATE userdata SET partnerships = {int(r2[0])+1} WHERE user_id = {event.member.id} AND guild_id = {event.get_guild().id}")
        msg = await partners_plugin.bot.rest.create_message(int(r[0]), hikari.Embed(title="Nawiązano partnerstwo", description=f"""<@{event.author.id}> dziękujemy za nawiązanie partnerstwa! To Twoje **{int(r2[0])+1}** partnerstwo. Otrzymujesz za to `{int(r2[0])+1*r3[1]}`$ {partner_msg}""", colour="#2F3136"))
        #user_balance = await client.edit_user_balance(guild_id, event.member.id, cash=int(int(r2[0])+1*r3[1]), reason="Partnerstwo")
    else:
        pass

@partners_plugin.listener(hikari.MemberDeleteEvent)
async def on_leave(event: hikari.Event) -> None:
    async with partners_plugin.bot.d.db.acquire() as con:
        c = await con.cursor()

    await c.execute(f'SELECT partner, ad_link FROM userdata WHERE user_id = {event.user_id} AND guild_id = {event.get_guild().id}')
    r = await c.fetchone()

    if str(r[0]) != 'Nie':
        await c.execute(f'SELECT log_channel FROM channels WHERE guild_id = {event.get_guild().id}')
        log_channel = await c.fetchone()

        if r is None:
            return
        
        await partners_plugin.bot.rest.create_message(int(log_channel[0]), hikari.Embed(title="Odpalono bota", description=f'Partner <@{event.user_id}> wyszedł z serwera. Podany wcześniej link do jego rekalmy to - {r[1]}', color='#ff0000'))

def load(bot):
    bot.add_plugin(partners_plugin)

def unload(bot):
    bot.remove_plugin(partners_plugin)

