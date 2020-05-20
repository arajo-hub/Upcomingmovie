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
    title=[]
    code=[]
    dateNcode=[]
    valueList=[]

    response=urlopen('https://movie.naver.com/movie/running/premovie.nhn')
    soup=BeautifulSoup(response,'html.parser')

    for anchor in soup.select('li>dl>dt>a'):
        link=anchor['href']
        code.append(link[link.index('=')+1:])
        movie[anchor.get_text()]=''
        title.append(anchor.get_text())

    opening_date=[]

    for anchor in soup.select('li>dl>dd:nth-child(3)>dl>dd'):
        if "개봉" in anchor.get_text():
            opening_date.append(anchor.get_text().split()[-2])
        else:
            pass

    for i in range(len(code)):
        dateNcode.append(code[i])
        dateNcode.append(opening_date[i])
        valueList.append(dateNcode)
        dateNcode=[]

    for i in range(len(title)):
        movie[title[i]]=valueList[i]

    return movie

cur=con.cursor()
cur.execute('SELECT * FROM parsed_data_parsed_movie')

if __name__=='__main__':
    movie_dict=parse_movie()
    for t, dNc in movie_dict.items():
        parsed_movie(title=t, date=dNc[0], code=dNc[1]).save()
