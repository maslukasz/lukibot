import mysql.connector

con = mysql.connector.connect(
  host="127.0.0.1",
  port=1433,
  user="bot",
  password="haslodobota1",
  db='thendbot', autocommit=True
)
c = con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS userdata(guild_id varchar(255),
user_id varchar(255),
xp INT,
level INT,
partnerships INT,
about varchar(255));""")

c.execute("""CREATE TABLE IF NOT EXISTS history_users (guild_id varchar(255),
	user_id	varchar(255),
	channel	varchar(255),
	data	TEXT,
	messages INTEGER);""")

c.execute("""CREATE TABLE IF NOT EXISTS embeds(guild_id varchar(255),
author_id varchar(255),
content varchar(2000),
colour TEXT,
primary key(guild_id))""")

c.execute("""CREATE TABLE IF NOT EXISTS config_values(guild_id varchar(255),
xp_system BOOL DEFAULT (FALSE),
min_xp INTEGER,
max_xp INTEGER,
partnership_earning INTEGER DEFAULT (5),
partnership_multiplier INTEGER DEFAULT (2),
partnership_rank TEXT,
partnerships_channel TEXT,
log_channel TEXT)""")

c.execute("""CREATE TABLE IF NOT EXISTS channels(guild_id varchar(255),
ignored varchar(255))""")

"""create table partners(guild_id text,
user_id text,
ad_link text,
ad text """