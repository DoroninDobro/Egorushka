import re
import csv
import json
import sqlite3
import requests
from bs4 import BeautifulSoup

all_rep = dict()
list_links = []

# here BS method
r = requests.get('http://www.gr-oborona.ru/texts/')
soup = BeautifulSoup(r.text, 'lxml')
div = soup.find_all('a')
# we make list all links songs
for a in div:
    link = a.get('href')
    if link[:6] == '/texts':
        list_links.append('http://www.gr-oborona.ru' + link)
# we make list all links songs
for link in list_links:
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'lxml')
    # we add song's name in our dict
    div = str(soup.find('h3'))
    name = div[4:]
    name = name[:-5]
    # we add song's name in our dict
    # we formatting song's text
    find_text = soup.find('div', {'id': 'cont'})
    rega = re.compile(r'Альбом:(.*?)<strong>')
    find_text = rega.findall(str(find_text))
    rega2 = re.compile(r'</p>(.*?)<p>')
    find_text = rega2.findall(str(find_text))
    find_text = str(find_text)
    find_text = find_text.replace('["', '').replace('\\xa0', ' ').replace('\\', '').replace('<br/>', '\n').replace('"]', '')
    # we formatting song's text
    all_rep[name] = find_text
# here we save our dict
json.dump(all_rep,open("dict_final.json","w"))
# here we save our dict
# and here we open our dict and save in csv for search
js = open("dict_final.json").read()
dict_songs = json.loads(js)
with open('all_songs.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(('Название','Текст'))
    for song in dict_songs:
        writer.writerow((song, dict_songs[song]))
# and here we open our dict and save in csv for search