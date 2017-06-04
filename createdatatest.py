import psycopg2

rows = ({'sign': 0, 'name': 'Zero'},
        {'sign': 1, 'name': 'Item One'},
        {'sign': 2, 'name': 'Item Two'},
        {'sign': 3, 'name': 'Three'})

conn =psycopg2.connect(database="pipeline", user="postgres", password="123", host="localhost", port="5432")
cur = conn.cursor()

# cur.execute("DELETE FROM user_tbl")
fg=cur.executemany("INSERT INTO user_tbl VALUES (%(sign)s, %(name)s)", rows)
conn.commit()
conn.close()