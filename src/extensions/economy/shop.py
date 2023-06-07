import hikari
import lightbulb
import miru

shop_plugin = lightbulb.Plugin("Plugin shop_plugin")

@shop_plugin.command
@lightbulb.command("shop", "shop", aliases=["sklep"])
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def shop(ctx: lightbulb.Context) -> None:
    await ctx.respond(hikari.Embed(title="Główna karta sklepu",
description="""Sklep dzieli się na kategorie:
`1.` **premium**,
`2.` **usługi**,
`3.` **kolory**,
`4.` **dodatki**.

Żeby otworzyć wybraną kartę wystarczy wpisać `,sklep <nazwa kategorii>`.""", colour='#7289da'))


class PremiumView(miru.View):

    @miru.button(label="VIP", emoji='⭐', style=hikari.ButtonStyle.SECONDARY)
    async def vip_button(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.respond(hikari.Embed(title="Korzyści roli VIP",
        description="""
● Co 12 godzin 500$.
● Unikatowa ranga <@&630485271221108766>.
● Nagroda za bump wzrasta o 5$.
● Paleta zmieniania sobie kolorów nicku.
● Możliwość nielimitowanej zmiany pseudonimu.
● 1000$ za zaakceptowaną sugestię.
● Specjalna naklejka.
● Wykonanie kanału milowego.""", color='#ffd858'), flags=hikari.MessageFlag.EPHEMERAL)

    @miru.button(label="Premium", emoji='🌟', style=hikari.ButtonStyle.SECONDARY)
    async def premium_button(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.respond(hikari.Embed(title="Korzyści roli Premium",
        description="""● Co 12 godzin 1000$.
● Unikatowa ranga <@&630485155274031105>.
● Nagroda za bump wzrasta o 10$.
● Paleta zmieniania sobie kolorów nicku.
● Możliwość nielimitowanej zmiany pseudonimu.
● 1200$ za zaakceptowaną sugestię.
● Wykonanie kanału milowego.""", color='#57ffad'), flags=hikari.MessageFlag.EPHEMERAL)

    @miru.button(label="Supreme", emoji='💫', style=hikari.ButtonStyle.SECONDARY)
    async def supreme_button(self, button: miru.Button, ctx: miru.Context):
        await ctx.respond(hikari.Embed(title="Korzyści roli Supreme",
        description="""● Co 12 godzin 1500$.
● Unikatowa ranga <@&688445563934474364>.
● Dostęp do unikatowej skrzyni.
● Specjalny kolor dla użytkownika z wybranym HEX'em.
● Nagroda za bump wzrasta o 15$.
● Dodatkowa nagroda za bump w tej samej wysokości co VIP.
● Paleta zmieniania sobie kolorów nicku.
● Możliwość nielimitowanej zmiany pseudonimu.
● 1500$ za zaakceptowaną sugestię.
● Wykonanie kanału milowego.""", color='#ff5e93'), flags=hikari.MessageFlag.EPHEMERAL)

    @miru.button(label='Bogacz', emoji='💸', style=hikari.ButtonStyle.SECONDARY)
    async def bogacz_button(self, button: miru.Button, ctx: miru.Context):
        await ctx.respond(hikari.Embed(title="Korzyści roli VIP",
        description="""● Co 12h 2000$.
● Unikatowa ranga <@&698989932772851715>.
● Skrzynia bogacza.
● Specjalny kolor dla użytkownika z wybraną emotką i HEX'em.
● Nagroda za bump wzrasta o 30$.
● Dodatkowa nagroda za bump w tej samej wysokości co VIP i Premium.
● Paleta zmieniania sobie kolorów nicku.
● Możliwość nielimitowanej zmiany pseudonimu.
● 1700$ za zaakceptowaną sugestię.
● Wykonanie kanału milowego.
""", color='#c9ff60'), flags=hikari.MessageFlag.EPHEMERAL)
    
    @miru.button(label='Szejk', emoji='👳', style=hikari.ButtonStyle.SECONDARY)
    async def szejk_button(self, button: miru.Button, ctx: miru.Context):
        await ctx.respond(hikari.Embed(title="Korzyści roli VIP",
        description="""● Co 12h 2500$.
● Unikatowa ranga <@&698989933188350082>.
● Specjalny kolor dla użytkownika z wybraną emotką i HEX'em.
● Nagroda za bump wzrasta o 50$.
● Dodatkowa nagroda za bump w tej samej wysokości co VIP, Premium, Premium+ i Bogacz.
● Paleta zmieniania sobie kolorów nicku.
● Możliwość nielimitowanej zmiany pseudonimu.
● 2000$ za zaakceptowaną sugestię.
● Wykonanie kanału milowego.
● Dostęp do modułu muzycznego w naszym autorskim bocie.""", color='#ffad4a'), flags=hikari.MessageFlag.EPHEMERAL)

@shop.child
@lightbulb.command("premium", "role premium sub")
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def premium(ctx: lightbulb.Context) -> None:
    view = PremiumView()  # Create a new view
    resp = await ctx.respond(hikari.Embed(title="Role premium",
    description="""`1.` Rola <@&630485271221108766> | **110 000** <:thend:742800976636936202>
`2.` Rola <@&630485155274031105> | **150 000** <:thend:742800976636936202>
`3.` Rola <@&688445563934474364> | **250 000** <:thend:742800976636936202>
`4.` Rola <@&698989932772851715> | **500 000** <:thend:742800976636936202>
`5.` Rola <@&698989933188350082> | **1 000000** <:thend:742800976636936202>
[```Kliknij guzik, żeby przeczytać korzyści konkretnej roli lub naciśnij na tę wiadomośc, aby teleportować się na wprowadzenie.```](https://discord.com/channels/630462196589264945/630462459458748417/827227351749230622)""", colour="#4F545C"), components=view.build())
    message = await resp.message()
    view.start(message)  # Start listening for interactions
    await view.wait() 

class UslugiViev(miru.View):
    @miru.button(label="Ticket ogłoszeń", emoji='🧠', style=hikari.ButtonStyle.PRIMARY)
    async def ticket_button(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.respond(hikari.Embed(title="Ticket ogłoszeń",
        description="""Możliwość wysłania 1 ogłoszenia na <#737431057686593597>.
● Ogłoszenie może być reklamą.
● Ogłoszenia nie zawierają wzmianek.""", colour='F4ABBA'), flags=hikari.MessageFlag.EPHEMERAL)

@shop.child
@lightbulb.command("usługi", "usługi sub", aliases=['uslugi'])
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def uslugi(ctx: lightbulb.Context) -> None:
    view = UslugiViev()
    resp = await ctx.respond(hikari.Embed(title="Usługi",
    description="""`1.` Ticket ogłoszeń | **90 000** <:thend:742800976636936202>""", color='#6b00a8'), components=view.build())
    message = await resp.message()
    view.start(message)
    await view.wait()


@shop.child
@lightbulb.command("kolory", "kolory sub")
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def kolory(ctx: lightbulb.Context) -> None:
    await ctx.respond(hikari.Embed(title="Kolory",
    description="""Każdy kolor kosztuje **100 000** <:thend:742800976636936202>
`1`. <@&690245468365652012>
`2.` <@&689662720039059546>
`3.` <@&688134141190996001>
`4.` <@&688133947632123974>
`5.` <@&688134526106730578>
`6.` <@&717038563593551884>
`7.` <@&716915038153080864>
`8.` <@&717038568366669986>
`9.` <@&716915036634742884>
`10.` <@&717038565372198952>
`11.` <@&690245469187997747>
`12.` <@&688134619731722240>
`13.` <@&688134252440846391>
`14.` <@&689662738133417992>
`15.` <@&688134445332561955>
`16.` <@&716915038916444211>
`17.` <@&717038566818971769>
`18.` <@&717038561505050694>
`19.` <@&717038559537660066>
`20.` <@&688133448770387989>""", color='#d3d0d0'))

@shop.child
@lightbulb.command("dodatki", "dodatki sub")
@lightbulb.implements(lightbulb.PrefixSubCommand)
async def dodatki(ctx: lightbulb.Context) -> None:
    await ctx.respond(hikari.Embed(title="Dodatki",
    description="""`1.` Ranga opisująca Ciebie - <@&727190590000857121> | **80 000** <:thend:742800976636936202>
`2.` Ranga opisująca Ciebie - <@&727190590873141251> | **80 000** <:thend:742800976636936202>
`3.` Ranga opisująca Ciebie - <@&727190592400130090> | **80 000** <:thend:742800976636936202>
`4.` Ranga opisująca Ciebie - <@&727190588650291220> | **80 000** <:thend:742800976636936202>""", colour='f3a9ff'))

def load(bot):
    bot.add_plugin(shop_plugin)

def unload(bot):
    bot.remove_plugin(shop_plugin)


