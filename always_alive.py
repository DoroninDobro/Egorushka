import os
import sqlite3
from sqlite3 import Error
from random import randint


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_read_select(connection, select):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(select)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



def always_alive(citations):
    if len(citations) > 0:
        for _ in range(len(citations) * 2):
            try:
                n = randint(1, len(citations))
                l_text = str(citations[n][1])
                c_point = l_text.find(cit)
                l_point = l_text[:c_point].rfind('\n\n')
                r_point = l_text[c_point:].find('\n\n') + c_point
                print(l_text[l_point:r_point].strip())
                print('Из песни:', citations[n][0])
                return 'nihuya'
            except:
                continue
        print('Всегда живой!')
    else:
        print('Всегда живой!')


cit = input('Введи текст: ').lower()
os.chdir('Egor')
connection = create_connection("Egor.db")
select_citations = f"""
SELECT name, text 
FROM songs
WHERE lower(text) LIKE '%{cit}%'
"""
citations = execute_read_select(connection, select_citations)
always_alive(citations)