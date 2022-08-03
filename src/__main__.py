import hikari
import lightbulb
import miru



import sqlite3

con = sqlite3.connect('main.db')
c = con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS userdata(
        userid bigint PRIMARY KEY,
        xp int DEFAULT 0,
        level int DEFAULT 0,
        messages int DEFAULT 0,
        money int DEFAULT 0)""")

bot = lightbulb.BotApp(prefix=";", token="NTY5OTI0NjUyMDg4OTUwNzk1.G4PEsK.T2SIKSA3Mr9-DHvAdWt8jur4cZp-O_xg1EaemQ", intents=hikari.Intents.ALL, help_class=None)



bot.load_extensions_from("./src/extensions")
bot.load_extensions_from("./src/economy")
bot.load_extensions_from("./src/plugins")
bot.load_extensions_from("./src/tekstowe")
bot.load_extensions_from("./src/user")

#bot.listen(hikari.MemberCreateEvent)
#async def on_joined(event: hikari.MemberCreateEvent) -> None:

@bot.listen()
async def on_starting(event: hikari.StartingEvent) -> None:
    await bot.rest.create_message(874675093354201148, hikari.Embed(
        title="Odpalono bota",
        description="""Bot został pomyślnie uruchiomiony. 

💻 **Dodatkowe dane**:
niebawem.""", colour="#36393e"))

#@bot.listen(lightbulb.events.CommandErrorEvent)
#async def on_command_error(event : lightbulb.events.CommandErrorEvent):
#    if isinstance(event.exception, lightbulb.errors.CommandIsOnCooldown):
#        await bot.create_message(f"{event.bot.cross} This command is on cooldown.")
#    else:
#        print(event.exception)
#        await bot.rest.create_message(874675093354201148, hikari.Event(titel='test'))


miru.load(bot)
bot.run()
