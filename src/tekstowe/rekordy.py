import hikari 
import lightbulb
import miru

import json

rekordy_ext = lightbulb.Plugin("Gablota :weary:")

class RekordyView(miru.View):
    @miru.button(label="Pierwsza strona", style=hikari.ButtonStyle.PRIMARY)
    async def pierwsza_strona(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.respond(hikari.Embed(title="Pierwsza Strona",
    description=f"""> <:kropka:756964971300257814>Najwięcej wiadomości na <#688507273198436385> - **18992**. Ustanowione przez <@415815804823797760>.
> <:kropka:756964971300257814>Najwięcej napisanych wiadomości na <#688507189383659547> - **34461**. Ustanowione przez <@415815804823797760>.
> <:kropka:756964971300257814>Najwięcej napisanych wiadomości przez miesiąc na <#688507189383659547> - **8937**. Ustanowione przez <@415815804823797760>.
> <:kropka:756964971300257814>Najwięcej napisanych wiadomości przez tydzień na <#688507189383659547> - **3100**. Ustanowione przez <@415815804823797760>.
> <:kropka:756964971300257814>Najwięcej napisanych wiadomości przez 24 godziny na <#688507189383659547> - **418**. Ustanowione przez <@415815804823797760>.
> <:kropka:756964971300257814>Najwięcej wygranych giveaway'ów - **3**. Ustanowione przez <@!418486004744454164>.
> <:kropka:756964971300257814>Najwięcej nadesłanych zaakceptowanych sugestii - **1**. Ustanowione przez <@!418486004744454164>.
> <:kropka:756964971300257814>Najdłuższy czas spędzony na kanałach głosowych przez tydzień - **5040 minut**. Ustanowione przez <@415815804823797760>.
> <:kropka:756964971300257814>Najdłuższy czas spędzony na kanałach głosowych przez miesiąc - **21600 minut**. Ustanowione przez <@415815804823797760>.
> <:kropka:756964971300257814>Najdłuższy czas spędzony na kanałach głosowych przez 24 godziny - **1440 minut**. Ustanowione przez <@!415815804823797760>.
> <:kropka:756964971300257814>Najwięcej wygranych wydarzeń - **Brak**.
> <:kropka:756964971300257814>Najwięcej zebranych reakcji pozytywnych pod memem - **12**. Ustanowione przez <@!418486004744454164>.""", colour="#5865F2"), flags=hikari.MessageFlag.EPHEMERAL)

    @miru.button(label="Druga strona", style=hikari.ButtonStyle.SUCCESS)
    async def druga_strona(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.respond(hikari.Embed(title="Druga strona",
    description=f"""> <:kropka:756964971300257814>Najwięcej otworzonych podstawowych boxów - **Brak**.
> <:kropka:756964971300257814>Najwięcej otworzonych srebrnych boxów - **Brak**.
> <:kropka:756964971300257814>Najwięcej otworzonych złotych boxów - **7**. Ustanowione przez <@!418486004744454164>.
> <:kropka:756964971300257814>Najwięcej zaproszonych osób - **Brak**.
> <:kropka:756964971300257814>Najwięcej wysłanych zdjęć na <#688516778405527671> - **38**. Ustanowione przez <@!415815804823797760>.
> <:kropka:756964971300257814>Bycie najwięcej razy Opiekunem Tygodnia - **Brak**.
> <:kropka:756964971300257814>Najwięcej napisanych recenzji na <#688698648191959134> - **Brak**.
> <:kropka:756964971300257814>Najwięcej napisanych recenzji na <#688698902131900418> - **8**. Ustanowione przez <@!351722490487373834>.
> <:kropka:756964971300257814>Najwięcej napisanych recenzji na <#688698993634574346> - **Brak**.
> <:kropka:756964971300257814>Najwięcej wysłanych prac na <#695392323495788686> - **Brak**.
> <:kropka:756964971300257814>Najwięcej wysłanych wiadomości na <#688515622337904708> - **129**. Ustanowione przez <@415815804823797760>.
> <:kropka:756964971300257814>Najwięcej bumpów - **6**. Ustanowione przez <@!418486004744454164>.
> <:kropka:756964971300257814>Najwięcej zdobytych level up'ów w ciągu 24 godzin - **4**. Ustanowione przez <@!418486004744454164>.
> <:kropka:756964971300257814>Najwięcej wysłanych <:honkhonk:711285475067035708> na <#688507189383659547> - **822**. Ustanowione przez <@415815804823797760>.
> <:kropka:756964971300257814>Najwięcej wpisanych komend `.work` na <#688507273198436385> - **1591**. Ustanowione przez <@415815804823797760>.""", colour="#5865F2"), flags=hikari.MessageFlag.EPHEMERAL)
@rekordy_ext.command 
@lightbulb.command('rekordy', 'rekordy')
@lightbulb.implements(lightbulb.PrefixCommand)
async def rekordy(ctx: lightbulb.Context) -> None:
    view = RekordyView()
    resp = await ctx.respond(hikari.Embed(title="Kategorie",
    description="""<:kropka:756964971300257814>Jak już pewnie mogłeś/-aś zauważyć, na The End wynagradzamy wszystkich aktywnych. Każdy lubi rywalizację. Każdy lubi wygrywać. Dlatego przygotowujemy dla was **Księgę rekordów The End**. Jest to proste - odpowiednik __Księgi rekordów Guinnessa__. Każdy może się tu znaleźć. Bijemy poprzedni rekord i ustanawiamy następny. Dla większej zabawy, dajemy możliwość wymyślania własnych rekordów. Na start podajemy kilka możliwości rekordów do pobicia, ale z dnia na dzień, możesz wpisać swój własny rekord.
<:kropka:756964971300257814>Za ustanowienie rekordu dostaniesz 500-10000 <:thend:742800976636936202>.
<:kropka:756964971300257814>System zgłaszania rekordów polega na przygotowaniu dowodów i udokumentowania tego na <#688510365549592634>.""", color='#ae74ff'), components=view.build())
    message = await resp.message()
    view.start(message)
    await view.wait()

def load(bot):
    bot.add_plugin(rekordy_ext)

def unload(bot):
    bot.remove_plugin(rekordy_ext)