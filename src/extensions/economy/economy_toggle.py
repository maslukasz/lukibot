import hikari
import lightbulb

from unbelipy import UnbeliClient

UNB_API_TOKEN  ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiIxMDU0ODAyNzA2NTA3NjMwNjgwIiwiaWF0IjoxNjg0NjA0MjQ3fQ.iJtRfMT1AuCVc0GGW7GPUZAp6vkgeGBGFLPiUs_RZdc" 
unbeliclient = UnbeliClient(token=UNB_API_TOKEN)

buy_ext = lightbulb.Plugin("buy", "buy")

@buy_ext.command
@lightbulb.command('economy-toggle', 'Włączanie i wyłączanie rozszerzenia do ekonomii.')
@lightbulb.implements(lightbulb.SlashCommand)
async def economy_toggle(ctx: lightbulb.Context) -> None:
    async with buy_ext.bot.d.db.acquire() as con:
        c = await con.cursor()
    #await c.execute(f'SELECT money FROM userdata WHERE userid = {ctx.member.id}')
    #r = await c.fetchone()

    edited_balance = await unbeliclient.edit_user_balance(
            guild_id=ctx.guild_id, 
            user_id=ctx.author.id,
            cash=100,
            reason="Test"
        )
    await ctx.respond("Przełączono")


def load(bot):
    bot.add_plugin(buy_ext)

def un_load(bot):
    bot.remove_plugin(buy_ext)
