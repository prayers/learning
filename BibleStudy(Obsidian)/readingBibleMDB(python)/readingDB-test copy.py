import sqlite3

conn = sqlite3.connect('bible_简体中文和合本.db')

cursor = conn.cursor()

sql = """select name from sqlite_master where type='table' order by name"""

cursor.execute(sql)

result = cursor.fetchall()

for res in result:
    print(res)
    # print(type(res))

"""_summary_
"""
sql2 = """pragma table_info(BibleID)"""
cursor.execute(sql2)
ress = cursor.fetchall()
print(ress)

#################
conn.close()
