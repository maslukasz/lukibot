import hikari
import lightbulb
import miru

import aiomysql

with open("./src/secrets/token") as f:
    _token = f.read().strip()

bot = lightbulb.BotApp(prefix=";", token=_token, intents=hikari.Intents.ALL, help_class=None)

# Ładowanie komend i eventów
bot.load_extensions_from("./src/extensions")
bot.load_extensions_from("./src/economy")
bot.load_extensions_from("./src/plugins")
bot.load_extensions_from("./src/tekstowe")
bot.load_extensions_from("./src/user")

#bot.listen(hikari.MemberCreateEvent)
#async def on_joined(event: hikari.MemberCreateEvent) -> None:
# Do zrobienia przy powitaniach

@bot.listen()
async def start(event: hikari.StartingEvent) -> None:
    await bot.rest.create_message(874675093354201148, hikari.Embed(title="Odpalono bota", description="""Bot został pomyślnie uruchiomiony.

💻 **Dodatkowe dane**:
niebawem.""", colour="#2F3136"))
    bot.d.db = await aiomysql.create_pool(host='127.0.0.1', user='bot', password='bot', db='thendbot', autocommit=True)

#@bot.listen(lightbulb.events.CommandErrorEvent)
#async def on_command_error(event : lightbulb.events.CommandErrorEvent):
    #if isinstance(event.exception, lightbulb.errors.CommandIsOnCooldown):
        #await bot.create_message(f"{event.bot.cross} This command is on cooldown.")
    #else:
        #print(event.exception)
        #await bot.rest.create_message(874675093354201148, hikari.Event(titel='test'))

miru.load(bot)
bot.run()
