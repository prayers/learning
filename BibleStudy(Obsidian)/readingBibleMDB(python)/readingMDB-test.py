import mdbtools

conn = mdbtools.connect('bible_简体中文和合本.mdb')

table_data = mdbtools.get_table(conn, 'table1')

for row in table_data:
    print(row)
