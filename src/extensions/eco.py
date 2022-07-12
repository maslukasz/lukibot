import hikari
import lightbulb

import requests
import random
import json

eco_plugin = lightbulb.Plugin("Ustawienia ekonomii - admin")




@eco_plugin.command()
#@lightbulb.add_cooldown(10, 1, lightbulb.cooldowns.UserBucket)
@lightbulb.command("mine", "work")
@lightbulb.implements(lightbulb.PrefixCommand)
async def mine(ctx: lightbulb.Context) -> None:
    
    with open ('src/items/surowce.json') as f:
        surowce = json.load(f)
    
    surowce_r = surowce['surowce'][random.randint(0, 5)]['type']['emoji']
    
    value = random.randint(1, 5)
    print(surowce)

    if surowce_r == 'kamien':
        value = 1
    elif surowce_r == 'metal':
        value = random.randint(1, 5)
    elif surowce_r == 'zloto':
        value = random.randint(2, 6)
    elif surowce_r == 'ametyst':
        value = random.randint(3, 7)
    elif surowce_r == 'szmaragd':
        value = random.randint(4, 8)
    elif surowce_r == 'szafir':
        value = random.randint(5, 9)

def load(bot):
    bot.add_plugin(eco_plugin)


def unload(bot):
    bot.remove_plugin(eco_plugin)
