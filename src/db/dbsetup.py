import asyncio 
import aiomysql

loop = asyncio.get_event_loop()

async def base(loop):
    conn = await aiomysql.connect(host='127.0.0.1', user='bot', password='bot', db='thendbot', loop=loop, autocommit=True)
    c = await conn.cursor()
    print("Połączono z bazą danych")

    async def execute(sql):
        await c.execute(sql)

    conn.close()

loop.run_until_complete(base(loop))

