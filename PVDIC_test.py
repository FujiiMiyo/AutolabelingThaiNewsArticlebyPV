# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 05:43:11 2018

@author: RIKO
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 23:25:01 2018


"""

import numpy as np
import pymysql
import pandas as pd
#import NLPS as nlp
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import stopwords
from pandas import Series,DataFrame
#import time
from gensim import models
from gensim import corpora,matutils
from gensim.models import word2vec


conn = pymysql.connect(host = 'localhost', user = 'root', passwd = None, db = 'dailynews', charset = 'utf8')
cur = conn.cursor()
cur.execute("USE dailynews")

class doc_labeling(object):
    
    ####### Get data #######
    def get_body_eco(self,limit):
        genre = []
        body = []
        
        cur.execute("SELECT genre FROM article WHERE genre LIKE '%economic%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            genre.append(k)
        
        cur.execute("SELECT body FROM article WHERE genre LIKE '%economic%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            body.append(k)
        #print(body)
        
        df = pd.DataFrame({'genre':genre,'body':body})
        #print(df)
        return df
    
    
    def get_body_ent(self,limit):
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
        #print(df)
        return df
    
    
    def get_body_fore(self,limit):
        genre = []
        body = []
        
        cur.execute("SELECT genre FROM article WHERE genre LIKE '%foreign%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            genre.append(k)
        
        cur.execute("SELECT body FROM article WHERE genre LIKE '%foreign%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            body.append(k)
        #print(body)
        
        df = pd.DataFrame({'genre':genre,'body':body})
        #print(df)
        return df
    
    
    def get_body_it(self,limit):
        genre = []
        body = []
        
        cur.execute("SELECT genre FROM article WHERE genre LIKE '%it%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            genre.append(k)
        
        cur.execute("SELECT body FROM article WHERE genre LIKE '%it%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            body.append(k)
        #print(body)
        
        df = pd.DataFrame({'genre':genre,'body':body})
        print(df)
        return df
    
    
    def get_body_spo(self,limit):
        genre = []
        body = []
        
        cur.execute("SELECT genre FROM article WHERE genre LIKE '%sports%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            genre.append(k)
        
        cur.execute("SELECT body FROM article WHERE genre LIKE '%sports%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            body.append(k)
        #print(body)
        
        df = pd.DataFrame({'genre':genre,'body':body})
        print(df)
        return df
    
    
    '''def get_body_wom(self,limit):
        genre = []
        body = []
        
        cur.execute("SELECT genre FROM article WHERE genre LIKE '%women%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            genre.append(k)
        
        cur.execute("SELECT body FROM article WHERE genre LIKE '%women%' LIMIT " + str(limit))
        rows = cur.fetchall()
        for k in rows:
            body.append(k)
        #print(body)
        
        df = pd.DataFrame({'genre':genre,'body':body})
        print(df)
        return df'''
    
    
    
    ####### Labeling #######
    def LabeledLineSentence(self,documents,label_name):
        sentences = []
        
        for uid,line in enumerate(np.ndenumerate(documents)):
            #print(line[1])
            doc = self.Tokenize_word(line[1])
            mod = models.doc2vec.LabeledSentence(words = doc, tags = ['%s_%s' %(label_name,uid)])
            sentences.append(mod)
            print(doc,['%s_%s' %(label_name,uid)])
        return sentences
    
    
    
    ####### Word segmention #######    
    def Tokenize_word(self,text):
        
        ######## Thai word segment ########
        #word = word_tokenize(sent, engine='mm')
        #word = word_tokenize(sent, engine='newmm')
        sent = text[0].replace("'","")
        word = word_tokenize(sent, engine='deepcut') # use this method
        wword = [x.strip(' ') for x in word]
        words =[]
        for w in wword:
            if w not in stopwords.words('thai'):
                words = [str for str in words if str]
                words.append(w)
        return words
        
        ######## Eng word segment ########
        '''word = text[0]
        words = []
        for i in word.split(' '):
            words = [str for str in words if str]
            words.append(i)
        return words'''



    ####### Doc2vec #######
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
        
        model.save('model_dailynews_deepcut')
        #model.save('model_dailynews_en')
        #model.save('model_dailynews_mm')
        #model.save('model_dailynews_newmm')


if __name__ == '__main__':
    
    '''doclb = doc_labeling()
    entertainment = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/entertainment.csv')
    it = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/it.csv')
    all_pd = pd.concat([entertainment,it],axis=1)
    print(all_pd.columns)
    
    ent = all_pd['body_ent'].values
    #print(ent)
    ent_sent = doclb.LabeledLineSentence(ent,'entertainment')
    #print(ent_sent)
    
    itec = all_pd['body_it'].dropna().values
    #print(itec)
    it_sent = doclb.LabeledLineSentence(itec,'it')
    #print(it_sent)'''
    
    doclb = doc_labeling()
    a = doclb.get_body_eco(500)
    b = doclb.get_body_ent(500)
    c = doclb.get_body_fore(500)
    d = doclb.get_body_it(500)
    e = doclb.get_body_spo(500)
    #f = doclb.get_body_spo(500)
    
    eco = a['body'].dropna().values
    eco_sent = doclb.LabeledLineSentence(eco,'economic')
    ent = b['body'].dropna().values
    ent_sent = doclb.LabeledLineSentence(ent,'entertainment')
    fore = c['body'].dropna().values
    fore_sent = doclb.LabeledLineSentence(fore,'foreign')
    itec = d['body'].dropna().values
    it_sent = doclb.LabeledLineSentence(itec,'it')
    spo = e['body'].dropna().values
    spo_sent = doclb.LabeledLineSentence(spo,'sports')
    '''wom = f['body'].dropna().values
    wom_sent = doclb.LabeledLineSentence(wom,'women')'''
    
    all_list_vec = []
    all_list_vec.extend(eco_sent)
    all_list_vec.extend(ent_sent)
    all_list_vec.extend(fore_sent)
    all_list_vec.extend(it_sent)
    all_list_vec.extend(spo_sent)
    #all_list_vec.extend(it_sent)
    print(all_list_vec)
    d = doclb.doc_to_vec(all_list_vec)
    #print(d)
    
    n_sent = len(all_list_vec)
    print(n_sent)
