import hikari
import lightbulb
from lightbulb.ext import tasks
import miru

import aiomysql

with open("./src/secrets/token") as f:
    _token = f.read().strip()

bot = lightbulb.BotApp(prefix=";", token=_token, intents=hikari.Intents.ALL | hikari.Intents.MESSAGE_CONTENT, help_class=None)

# Ładowanie komend i eventów
bot.load_extensions_from("./src/extensions")
bot.load_extensions_from("./src/extensions/economy")
bot.load_extensions_from("./src/extensions/plugins")
bot.load_extensions_from("./src/extensions/tekstowe")
bot.load_extensions_from("./src/extensions/user")
bot.load_extensions_from("./src/extensions/moderation")

#bot.listen(hikari.MemberCreateEvent)
#async def on_joined(event: hikari.MemberCreateEvent) -> None:
# Do zrobienia przy powitaniach

@bot.listen()
async def start(event: hikari.StartingEvent) -> None:
#    await bot.rest.create_message(874675093354201148, hikari.Embed(title="Odpalono bota", description="""Bot został pomyślnie uruchiomiony.

#💻 **Dodatkowe dane**:
#niebawem.""", colour="#2F3136"))
    bot.d.db = await aiomysql.create_pool(host='192.168.0.134', user='bot', password='bot', db='thendbot', autocommit=True, minsize=15, maxsize=150)

#@bot.listen(lightbulb.events.CommandErrorEvent)
#async def on_command_error(event : lightbulb.events.CommandErrorEvent):
#    if isinstance(event.exception, lightbulb.errors.MissingRequiredRole):
#        await event.context.respond(f"{event.context.mode} This command is on cooldown.")
#    else:
#        print(event.exception)





miru.install(bot)
tasks.load(bot)
bot.run()
