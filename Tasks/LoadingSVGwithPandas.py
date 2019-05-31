import sqlite3
import pandas as pd

db_filename = 'test.db'
csv_filename = 'song_data.csv'
table = 'Songs'


with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE Songs (song_id, title, release, artist_name, year);")
    chunksize = 10 ** 5
    for chunk in pd.read_csv(csv_filename, delimiter=',', chunksize=chunksize):
        chunk.to_sql(table, conn, if_exists='append', index=False)

conn.commit()
conn.close()