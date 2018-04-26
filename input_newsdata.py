# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 16:46:46 2018


"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import sys

sys.setrecursionlimit(23000)

conn = pymysql.connect(host = 'localhost', user = 'root', passwd = None, db = 'dailynews', charset = 'utf8')

cur = conn.cursor()
cur.execute("USE dailynews")

random.seed(datetime.datetime.now())

cnt = 0
sql = cur.execute("SELECT URL FROM url_entertainment_test")
url = cur.fetchall()

def store(URL,title,genre,body,time):
    cur.execute("INSERT INTO entertainment(URL,title,genre,body,time) VALUES(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")",(URL,title,genre,body,time))
    cur.connection.commit()
    
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
    
def getLinks(articleUrl,genre):
    global cnt
    cnt +=1
    try:
        articleUrl = articleUrl.replace("\'", "")
        html = urlopen(articleUrl)
        bsObj = BeautifulSoup(html,"lxml")
        
        URL = articleUrl
        title = bsObj.find("h1").get_text()
        print(title)
        #body = bsObj.find("section",{"class":"article-detail"}).find(has_class_but_no_id).get_text().replace('\n', '').strip()
        body = bsObj.find("div",{"class":"entry textbox content-all"}).get_text().replace('\n', '').replace("'","").replace("(","").replace(")","").replace("\xa0","").replace("\r\n","").replace("\r","").replace(";","").replace("\t","").replace("\u200b","").replace("/","").replace("-","").replace("googletag.cmd.push","").replace("function","").replace("googletag.display","").replace("div","").replace("gpt","").replace("ad","").replace("8668011","").replace("{","").replace("}","").replace(",","").replace("\'","").replace("\"","").replace("!!","").replace("!","").replace(":","").replace("”","").replace("“","").replace("","").replace("?","").replace("{","").replace("}","").replace("’","").replace("‘","").replace("–","").replace(".","").replace("\[","").replace("\]","").strip()
        print(body)
        time = bsObj.find("span",{"class":"date"}).get_text()
        print(time)
        
        store(URL,title,genre,body,time)
        print(URL)
    except Exception:
        print(cnt)
        return 0
    
if __name__ == '__main__':
    for i in url:
        getLinks(i[0],"entertainment")
        
    print("finish")