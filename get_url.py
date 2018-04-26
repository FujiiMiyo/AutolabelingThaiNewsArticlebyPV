# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:08:02 2018


"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', passwd = None, db = 'dailynews', charset = 'utf8')

cur = conn.cursor()
cur.execute("USE dailynews")

random.seed(datetime.datetime.now())
count = 0

def store(URL):
    cur.execute("INSERT INTO url_entertainment_test(URL) VALUES (\"%s\")", (URL))
    cur.connection.commit()
    
def getLinks(genre,cnt):
    url = "https://www.dailynews.co.th/"+genre+"?page="+str(cnt)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    
    #article = bsObj.findAll("article", {"class":"card large newsItem"})
    
    for link in bsObj.findAll("a", href = re.compile("https://www.dailynews.co.th/"+genre+"/")):
        if 'href' in link.attrs:
            new_links = link.attrs['href']
            try:
                store(new_links)
                print(new_links)
            except Exception:
                continue
    
    if cnt < 40:
        cnt+=1
        print(cnt)
        getLinks(genre,cnt)
            
if __name__ == '__main__':
    getLinks('entertainment',1)