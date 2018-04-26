# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 00:36:03 2018


"""

from gensim import models
from collections import Counter
from sklearn.metrics import precision_recall_fscore_support

if __name__ == '__main__':
    
    ##### Load PV-DM Model #####
    #model = models.doc2vec.Doc2Vec(alpha=0.025, min_alpha=0.025)
    #model_loaded = models.doc2vec.Doc2Vec.load('model_dailynews_economic')
    model_loaded1 = models.doc2vec.Doc2Vec.load('model_dailynews_entertainment')
    #model_loaded2 = models.doc2vec.Doc2Vec.load('model_dailynews_foreign')
    model_loaded3 = models.doc2vec.Doc2Vec.load('model_dailynews_it_en')
    #model_loaded4 = models.doc2vec.Doc2Vec.load('model_dailynews_sports')
    #print(model_loaded)
    print(model_loaded1)
    #print(model_loaded2)
    #print(model_loaded3)
    #print(model_loaded4)
    
    
    ##### Article vectors Similar #####
    #print(model_loaded.docvecs.most_similar(["economic_392"]))
    #print(model_loaded1.docvecs.most_similar(["entertainment_3"]))
    #print(model_loaded2.docvecs.most_similar(["foreign_1"]))
    #print(model_loaded3.docvecs.most_similar(["it_13"]))
    #print(model_loaded4.docvecs.most_similar(["sports_356"]))
    
    #print(model_loaded1.docvecs.most_similar(["entertainment_252"])) #add
    
    
    ##### Word vectors Similar #####
    #print(model_loaded1.most_similar(["เอสเอ็ม"]))
    
    
    ##### Choose paragraph vectors Similar #####
    #vec = model_loaded.docvecs['economic_392']
    vec1 = model_loaded1.docvecs['entertainment_3']
    #vec2 = model_loaded2.docvecs['foreign_392']
    vec3 = model_loaded3.docvecs['it_367']
    #vec4 = model_loaded4.docvecs['sports_356']
    
    vec5 = model_loaded3.docvecs['it_356']
    vec6 = model_loaded1.docvecs['entertainment_5']
    #vec7 = model_loaded1.docvecs['entertainment_252']
    vec8 = model_loaded3.docvecs['it_65']
    #vec9 = model_loaded1.docvecs['entertainment_202'] ##target
    vec10 = model_loaded3.docvecs['it_13']
    vec12 = model_loaded3.docvecs['it_181']
    #vec13 = model_loaded1.docvecs['entertainment_176'] ##target
    
    #tasu = (vec1)
    tasu = (vec1+vec6)
    
    #tasu = (vec10)
    #tasu = (vec10+vec12)
    
    y = model_loaded1.similar_by_vector(tasu, topn=20, restrict_vocab=None)
    print(y)
    #z = model_loaded3.similar_by_vector(tasu, topn=20, restrict_vocab=None)
    #print(z)
    #a = model_loaded.most_similar('มือถือ')
    #print(a)