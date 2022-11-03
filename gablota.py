import hikari 
import lightbulb
import miru

import json

gablota_ext = lightbulb.Plugin("Gablota :weary:")

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

@gablota_ext.command 
@lightbulb.command('gablota', 'gablota')
@lightbulb.implements(lightbulb.PrefixCommand)
async def gablota(ctx: lightbulb.Cotnext) -> None:
    view = GablotaView()
    resp =await ctx.respond(hikari.Embed(title="Kategorie",
    description="""Gablota dzieli się na swoje kategorie. Za pomocą guzików dokonaj wyboru, ktorą częśc chcesz zobaczyć. Pamiętaj, że po wciśnięciu guzika tylko Ty będziesz widział/-a wiadomość.""", color='#ae74ff'))
    message = await resp.message()
    view.start(message)
    await view.wait()

def load(bot):
    bot.add_plugin(gablota_ext)

def unload(bot):
    bot.remove_plugin(gablota_ext)