import calendar
import sqlite3 as db
con = db.connect("main.db")
c = con.cursor()
c2 = con.cursor()
c3 = con.cursor()
import time
from datetime import timezone

import datetime

c.execute("SELECT * FROM 'history-users' WHERE userid = 342355402429825035")
r = c.fetchone()

print(r)