import os
import json
import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

os.chdir('Egor')
connection = create_connection("Egor.db")
create_songs_table = """
CREATE TABLE IF NOT EXISTS songs (
  name TEXT NOT NULL,
  text TEXT
);
"""
execute_query(connection, create_songs_table)
js = open("dict_final.json").read()
dict_songs = json.loads(js)

def fill_table(dict_songs):
    count = 0
    for song in dict_songs:
        create_song = f"""
        INSERT INTO
          songs (name, text)
        VALUES
          ("{song}", "{dict_songs[song]}");
        """ #% (song, dict_songs[song])
        execute_query(connection, create_song)
        count += 1
    print('Success load %i songs!' % count)
fill_table(dict_songs)
