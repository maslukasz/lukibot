import hikari
import lightbulb
import miru



import psycopg2

con = None
c = None

try:
    con = psycopg2.connect(
        host="localhost",
        dbname="demo",
        user='postgres',
        password='admin',
        port=5432)
    
    c = con.cursor()

    create_script = """CREATE TABLE IF NOT EXISTS userdata (
        userid int PRIMARY KEY,
        xp int NOT NULL DEFAULT 0,
        level int NOT NULL DEFAULT 0)"""
    c.execute(create_script)
    con.commit()

except Exception as error:
    print(error)

finally:
    if con is not None:
        con.close()
        
    if c is not None:
        c.close()


bot = lightbulb.BotApp(prefix=",", token="NTY5OTI0NjUyMDg4OTUwNzk1.G4PEsK.T2SIKSA3Mr9-DHvAdWt8jur4cZp-O_xg1EaemQ", intents=hikari.Intents.ALL, help_class=None)



bot.load_extensions_from("./src/extensions")
bot.load_extensions_from("./src/economy")
bot.load_extensions_from("./src/plugins")

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
