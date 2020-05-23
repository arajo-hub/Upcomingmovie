from bs4 import BeautifulSoup
from urllib.request import urlopen

import sqlite3
con=sqlite3.connect('./db.sqlite3')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","upcomingmovie.settings")
import django
django.setup()

from parsed_data.models import parsed_movie

def parse_movie():
    movie={}
    codes=[]
    title=[]
    opening_date=[]
    TitleDate=[]
    valueList=[]

    response=urlopen('https://movie.naver.com/movie/running/premovie.nhn')
    soup=BeautifulSoup(response,'html.parser')

    for anchor in soup.select('li>dl>dt>a'):
        link=anchor['href']
        code=link[link.index('=')+1:]
        codes.append(code)
        movie[code]=''
        title.append(anchor.get_text())

    for anchor in soup.select('li>dl>dd:nth-child(3)>dl>dd'):
        if "개봉" in anchor.get_text():
            opening_date.append(anchor.get_text().split()[-2])
        else:
            pass

    for i in range(len(title)):
        TitleDate.append(title[i])
        TitleDate.append(opening_date[i])
        valueList.append(TitleDate)
        TitleDate=[]

    for j in range(len(codes)):
        movie[codes[j]]=valueList[j]

    return movie

cur=con.cursor()
cur.execute('SELECT code FROM parsed_data_parsed_movie')
updateData=[]

if __name__=='__main__':
    movie_dict=parse_movie()

    for row in cur:
        if row[0] in movie_dict:
            print(row, "있음")
        else:
            cur.execute('DELETE FROM parsed_data_parsed_movie')
    con.commit()

    for key, value in movie_dict.items():
        try:
            parsed_movie(title=value[0], date=value[1], code=key).save()
        except:
            updateData.append((value[0], value[1], key))
    print(updateData)
    cur.executemany('UPDATE parsed_data_parsed_movie SET title=?, date=? WHERE code=?', updateData)
    con.commit()
    con.close()
