import sqlite3 as db
con = db.connect("main.db")
c = con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS userdata (
        userid bigint PRIMARY KEY,
        xp int DEFAULT 0,
        level int DEFAULT 0,
        money int DEFAULT 0)""")

c.execute("""CREATE TABLE IF NOT EXISTS "history-users" (
	"userid"	INTEGER,
	"channel"	INTEGER,
	"data"	TEXT,
	"messages"	INTEGER,
	PRIMARY KEY("data","channel","userid")
);""")