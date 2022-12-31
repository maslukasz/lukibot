import hikari
import lightbulb
from lightbulb.ext import tasks
import miru

import aiomysql

with open("./src/secrets/token") as f:
    _token = f.read().strip()

bot = lightbulb.BotApp(prefix="-", token=_token, intents=hikari.Intents.ALL, help_class=None)

# Ładowanie komend i eventów
bot.load_extensions_from("./src/extensions")
bot.load_extensions_from("./src/economy")
bot.load_extensions_from("./src/plugins")
bot.load_extensions_from("./src/tekstowe")
bot.load_extensions_from("./src/user")
bot.load_extensions_from("./src/moderation")

#bot.listen(hikari.MemberCreateEvent)
#async def on_joined(event: hikari.MemberCreateEvent) -> None:
# Do zrobienia przy powitaniach

@bot.listen()
async def start(event: hikari.StartingEvent) -> None:
#    await bot.rest.create_message(874675093354201148, hikari.Embed(title="Odpalono bota", description="""Bot został pomyślnie uruchiomiony.

#💻 **Dodatkowe dane**:
#niebawem.""", colour="#2F3136"))
    bot.d.db = await aiomysql.create_pool(host='127.0.0.1', port=1433, user='bot', password='haslodobota1', db='thendbot', autocommit=True, minsize=15, maxsize=150)

#@bot.listen(lightbulb.events.CommandErrorEvent)
#async def on_command_error(event : lightbulb.events.CommandErrorEvent):
#    if isinstance(event.exception, lightbulb.errors.MissingRequiredRole):
#        await event.context.respond(f"{event.context.mode} This command is on cooldown.")
#    else:
#        print(event.exception)
import datetime
from datetime import datetime, timedelta
@tasks.task(s=2, auto_start=False)
async def print_every_30_seconds():
    print('test')



miru.install(bot)
tasks.load(bot)
bot.run()
