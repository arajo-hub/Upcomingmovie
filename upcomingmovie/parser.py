from bs4 import BeautifulSoup
from urllib.request import urlopen

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","upcomingmovie.settings")
import django
django.setup()

from parsed_data.models import parsed_movie

def parse_movie():
    movie={}
    title=[]
    response=urlopen('https://movie.naver.com/movie/running/premovie.nhn')
    soup=BeautifulSoup(response,'html.parser')

    for anchor in soup.select('li>dl>dt>a'):
        movie[anchor.get_text()]=''
        title.append(anchor.get_text())

    opening_date=[]

    for anchor in soup.select('li>dl>dd:nth-child(3)>dl>dd'):
        if "개봉" in anchor.get_text():
            opening_date.append(anchor.get_text().split()[-2])
        else:
            pass

    for i in range(len(title)):
        movie[title[i]]=opening_date[i]

    return movie


if __name__=='__main__':
    movie_dict = parse_movie()
    for t, d in movie_dict.items():
        parsed_movie(title=t, date=d).save()
