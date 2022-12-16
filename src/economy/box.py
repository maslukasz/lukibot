import hikari 
import lightbulb

import hikari 
import lightbulb
import miru

import json

box_extension = lightbulb.Plugin("Gablota :weary:")

class GablotaView(miru.View):
    @miru.button(label="Ticket ogłoszeń", emoji='🧠', style=hikari.ButtonStyle.PRIMARY)
    async def ticket_button(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.respond(hikari.Embed(title="Użytkownicy Tygodnia",
        description="""""", colour='#94f0ff'), flags=hikari.MessageFlag.EPHEMERAL)

        with open("./json/ut.json", "r") as read_file:
            data = json.load(read_file)
        
        with open("./json/ut.json", "r") as read_file:
            data = json.load(read_file)

        await ctx.respond(hikari.Embed(title="Użytkownicy Tygodnia",
    description=f"""""", colour="#5865F2")
    .set_footer(text=f'Autorem komendy jest {data[ctx.options.rawka.lower()]["author"]}'))

@box_extension.command 
@lightbulb.command('boxy', 'Sprawdź informacje o boxach')
@lightbulb.implements(lightbulb.PrefixCommandGroup, lightbulb.SlashCommandGroup)
async def boxy(ctx: lightbulb.Context) -> None:
    await ctx.respond(hikari.Embed(title="Wszystko o boxach",
    description="""<:klucz:783657813065990164> **Wszystkie możliwe boxy**
<:blurpledot:925702134467551273> Drewniany (<:SkrzynkaDrewniania:780560981373747210>)
<:blurpledot:925702134467551273> Srebrny (<:SkrzynkaSrebrna:780561628487614486>)
<:blurpledot:925702134467551273> Złoty (<:SkrzynkaZota:780562333168697384>)
<:blurpledot:925702134467551273> Diamentowy (<:SkrzynkaDiamentowa:780563061051621397>)
<:blurpledot:925702134467551273> Szmaragdowy (<:SkrzynkaSzmaragdowa:780563551257362443>)
<:blurpledot:925702134467551273> Szafirowy (<:SkrzynkaSzafirowa:780564290942795837>)
<:blurpledot:925702134467551273> Mityczny (<:SkrzynkaMityczna:780568548040900659>)
<:blurpledot:925702134467551273> Legendarny (<:SkrzynkaLegendarna:781083464534589450>)

**<:BIomidkjaki:780401492611563560> Boxy z biomów**
<:blurpledot:925702134467551273> Wulkaiczny (<a:SkrzynkaWulkaniczna:780566966796288042>)

**<:thend:742800976636936202> Okresowe**
<:blurpledot:925702134467551273> Świąteczny (<:PodstawowaSwiateczna:783641657996345344>)

`💡` Najpierw musisz zdobyć boxa, żeby go otworzyć i stworzyć klucz (<:klucz:783657813065990164>). Do stworzenia klucza jest Ci potrzebne x12 <:Zloto:780397068320899083>""", color='#ae74ff'))


@boxy.child
@lightbulb.command("informacje", "Informacje o boxach")
@lightbulb.implements(lightbulb.PrefixSubCommand, lightbulb.SlashSubCommand)
async def loot(ctx: lightbulb.Context) -> None:
    await ctx.respond(hikari.Embed(title="Wszystko o boxach",
    description="""<:klucz:783657813065990164> **Wszystkie możliwe boxy**
<:blurpledot:925702134467551273> Drewniany (<:SkrzynkaDrewniania:780560981373747210>)
<:blurpledot:925702134467551273> Srebrny (<:SkrzynkaSrebrna:780561628487614486>)
<:blurpledot:925702134467551273> Złoty (<:SkrzynkaZota:780562333168697384>)
<:blurpledot:925702134467551273> Diamentowy (<:SkrzynkaDiamentowa:780563061051621397>)
<:blurpledot:925702134467551273> Szmaragdowy (<:SkrzynkaSzmaragdowa:780563551257362443>)
<:blurpledot:925702134467551273> Szafirowy (<:SkrzynkaSzafirowa:780564290942795837>)
<:blurpledot:925702134467551273> Mityczny (<:SkrzynkaMityczna:780568548040900659>)
<:blurpledot:925702134467551273> Legendarny (<:SkrzynkaLegendarna:781083464534589450>)

**<:BIomidkjaki:780401492611563560> Boxy z biomów**
<:blurpledot:925702134467551273> Wulkaiczny (<a:SkrzynkaWulkaniczna:780566966796288042>)

**<:thend:742800976636936202> Okresowe**
<:blurpledot:925702134467551273> Świąteczny (<:PodstawowaSwiateczna:783641657996345344>)

`💡` Najpierw musisz zdobyć boxa, żeby go otworzyć i stworzyć klucz (<:klucz:783657813065990164>). Do stworzenia klucza jest Ci potrzebne x12 <:Zloto:780397068320899083>""", color='#ae74ff'))


@boxy.child
@lightbulb.command("nagrody", "Opis możliwych nagród z poszczególnych boxów")
@lightbulb.implements(lightbulb.PrefixSubCommand, lightbulb.SlashSubCommand)
async def nagrody(ctx: lightbulb.Context) -> None:
    await ctx.respond("test")


def load(bot):
    bot.add_plugin(box_extension)

def unload(bot):
    bot.remove_plugin(box_extension)