import calendar
import sqlite3 as db
con = db.connect("main.db")
c = con.cursor()
c2 = con.cursor()
c3 = con.cursor()
import time
from datetime import timezone

import datetime

print(datetime.datetime.now())