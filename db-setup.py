import sqlite3 as db
con = db.connect("main.db")
c = con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS userdata (
        userid bigint PRIMARY KEY,
        xp int DEFAULT 0,
        level int DEFAULT 0,
        money int DEFAULT 0)""")

c.execute("""CREATE TABLE IF NOT EXISTS userstats (
        userid bigint PRIMARY KEY,
        messages bigint DEFAULT 0,
        messages7d int DEFAULT 0,
        messages30d int DEFAULT 0,
        aboutme TEXT DEFAULT "Nie ustawiono about me. Wpisz `,poradniki`, aby dowiedzieć się jak to zmienić!")""")