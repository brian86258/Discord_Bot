import sqlite3
db = sqlite3.connect('data.sqlite')

user_id = "741527663147220992"
cur = db.cursor()


exec = "Select tokens from users where user_id = '{}'".format(user_id)
res = cur.execute(exec).fetchone()
print(type(res[0]))

