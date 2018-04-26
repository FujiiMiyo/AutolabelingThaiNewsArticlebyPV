# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 00:46:38 2018


"""

from gensim import models
#import numpy as np
#import pymysql
#import pandas as pd
#import MeCab
#from progressbar import ProgressBar
#import time
#from pandas import Series,DataFrame
#from gensim import corpora,matutils
#from gensim.models import word2vec
#import math


if __name__ == '__main__':
    #model = models.doc2vec.Doc2Vec(alpha=0.025, min_alpha=0.025)
    
    ####### Load model ########
    model_loaded = models.doc2vec.Doc2Vec.load('model_dailynews1_deepcut_noeco_1500')
    #model_loaded1 = models.doc2vec.Doc2Vec.load('model_dailynews1_eng')
    #model_loaded2 = models.doc2vec.Doc2Vec.load('model_dailynews1_mm')
    #print(model_loaded)
    #print(model_loaded1)
    
    print(model_loaded.most_similar(["เทคโนโลยี"]))
    
    ######## Similar article ##########
    print(model_loaded.docvecs.most_similar(["it_245"]))

    
    ########## Similar word #############
    vec1 = model_loaded.docvecs['it_245']
    vec2 = model_loaded.docvecs['it_464']
    vec3 = model_loaded.docvecs['sports_1268']
    vec4 = model_loaded.docvecs['it_890']
    vec5 = model_loaded.docvecs['it_986']
    vec6 = model_loaded.docvecs['it_1061']
    vec7 = model_loaded.docvecs['it_876']
    vec8 = model_loaded.docvecs['it_622']
    vec9 = model_loaded.docvecs['it_1116']
    vec10 = model_loaded.docvecs['it_228']
    vec11 = model_loaded.docvecs['it_270']
    vec12 = model_loaded.docvecs['education_759']
    
       
    
    
    tasu = (vec1)
    tasu1 = (vec1+vec2+vec4)
    z = model_loaded.similar_by_vector(tasu, topn=20, restrict_vocab=None)
    print(z)
    y = model_loaded.similar_by_vector(tasu1, topn=20, restrict_vocab=None)
    print(y)

