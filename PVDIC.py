# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 23:25:01 2018


"""

import numpy as np
import pymysql
import pandas as pd
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import stopwords
from pandas import Series,DataFrame
#import time
from gensim import models
from gensim import corpora,matutils
from gensim.models import word2vec
#import math

conn = pymysql.connect(host = 'localhost', user = 'root', passwd = None, db = 'dailynews', charset = 'utf8')

cur = conn.cursor()
cur.execute("USE dailynews")

class MySystem(object):
    
    def get_body(self,limit):
        genre = []
        body = []
        
        cur.execute("SELECT genre FROM article WHERE genre LIKE '%entertainment%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            genre.append(k)
        
        cur.execute("SELECT body FROM article WHERE genre LIKE '%entertainment%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            body.append(k)
        #print(body)
        
        df = pd.DataFrame({'genre':genre,'body':body})
        
        return df
    
    
    def LabeledLineSentence(self,documents,label_name):
        sentences = []
        
        for uid,line in enumerate(np.ndenumerate(documents)):
            #print(line[1])
            doc = self.Tokenize_word(line[1])
            mod = models.doc2vec.LabeledSentence(words = doc, tags = ['%s_%s' %(label_name,uid)])
            sentences.append(mod)
            print(doc,['%s_%s' %(label_name,uid)])
        return sentences
        
    
    
    def Tokenize_word(self,text):
        
        ######## Thai word segment ########
        sent = text[0].replace("'","")
        #word = word_tokenize(sent, engine='mm')
        #word = word_tokenize(sent, engine='newmm')
        word = word_tokenize(sent, engine='deepcut') # use this method
        wword = [x.strip(' ') for x in word]
        words =[]
        
        for w in wword:
            if w not in stopwords.words('thai'):
                words = [str for str in words if str]
                words.append(w)
        return words
        
    
        ######## Eng word segment ########
        #word = text[0]
        #words = []
        #for i in word.split(' '):
            #words = [str for str in words if str]
            #words.append(i)
        #return words
    
    
    def doc_to_vec(self,documents):
        model = models.doc2vec.Doc2Vec(dm = 1, alpha=0.025, min_alpha=0.025) #use fixed learning rate
        model.build_vocab(documents)
        
        '''
        for epoch in range(10):
            model.train(documents, total_examples=10000, epochs=10)
            model.alpha -= 0.002 #decrease the learning rate
            model.min_alpha = model.alpha #fix the learning rate, no dacay            
        '''
        
        model.train(documents, total_examples=10000, epochs=10)
        
        #model.save('model_mm_dailynews_economic')
        #model.save('model_mm_dailynews_entertainment')
        #model.save('model_mm_dailynews_foreign')
        #model.save('model_mm_dailynews_it')
        #model.save('model_mm_dailynews_sports')
        
        #model.save('model_nmm_dailynews_economic')
        #model.save('model_nmm_dailynews_entertainment')
        #model.save('model_nmm_dailynews_foreign')
        #model.save('model_nmm_dailynews_it')
        #model.save('model_nmm_dailynews_sports')
        
        
        #model.save('model_dailynews_economic')
        model.save('model_dailynews_entertainment')
        #model.save('model_dailynews_foreign')
        #model.save('model_dailynews_it')
        #model.save('model_dailynews_sports')
        
    
if __name__ == '__main__':
    MS = MySystem()
    a = MS.get_body(1000)
    #print(a)
    #b = MS.Tokenize_word("จบไปแล้วใครยังฟินค้างอยู่ ไลค์รัวๆ กันได้เลย กับ 11 หนุ่มน้อยวัยฮอร์โมนพุ่งวง วอนนาวัน Wanna One กับการมาโชว์ที่ไทยเป็นครั้งแรกในงาน วอนนาวัน เฟิร์ส แฟน มีตติ้ง อิน แบงคอก : วอนนา บี เลิฟ WANNA ONE 1 st Fan Meeting in Bangkok : WANNA Be LovEd จัดไปแล้วที่ ไบเทคบางนา ฮอลล์ 106 แฟนคลับเกาหลีได้ฟินจังเพราะ กึ้ง เฉลิมชัย แห่งบริษัท โฟร์ วัน วัน เอ็นเตอร์เทนเม้นท์ นำมาให้ดูถึงไทยกันเลย")
    #print(b)
    b = a['body'].dropna().values
    b_sent = MS.LabeledLineSentence(b,'entertainment')
    #print(b_sent)
    
    c = MS.doc_to_vec(b_sent)
    print(c)