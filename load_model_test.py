# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 02:04:51 2018


"""

from gensim import models
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
import pandas as pd


if __name__ == '__main__':
    
    ####### Get data from CSV ########
    economic = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/economic.csv')
    entertainment = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/entertainment.csv')
    foreign = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/foreign.csv')
    it = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/it.csv')
    sports = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/sports.csv')
    all_pd = pd.concat([economic,entertainment,foreign,it,sports],axis=1)
    print(all_pd.columns)
    
    ####### Load model ########
    model = models.doc2vec.Doc2Vec(alpha=0.025, min_alpha=0.025)  # use fixed learning rate
    model_loaded = models.doc2vec.Doc2Vec.load('model_dailynews_en')
    
    ####### Create lists of labels and vectors ########
    all_label_vec = []
    all_list = []
    
    cnt = 0
    for i in all_pd['economic'].values:
        eco_vec = model_loaded.docvecs['economic_%s' %(cnt)]
        #print('%s' %(eco_vec))
        all_list.append(eco_vec)
        all_label_vec.append(0)
        cnt += 1
        
    cnt1 = 0
    for i in all_pd['entertainment'].values:
        ent_vec = model_loaded.docvecs['entertainment_%s' %(cnt1)]
        #print('%s' %(ent_vec))
        all_list.append(ent_vec)
        all_label_vec.append(1)
        cnt1 += 1
            
    cnt2 = 0
    for i in all_pd['foreign'].values:
        fore_vec = model_loaded.docvecs['foreign_%s' %(cnt2)]
        #print('%s' %(foreign_vec))
        all_list.append(fore_vec)
        all_label_vec.append(2)
        cnt2 += 1
        
    cnt3 = 0
    for i in all_pd['it'].values:
        it_vec = model_loaded.docvecs['it_%s' %(cnt3)]
        #print('%s' %(it_vec))
        all_list.append(it_vec)
        all_label_vec.append(3)
        cnt3 += 1
        
    cnt4 = 0
    for i in all_pd['sports'].values:
        spo_vec = model_loaded.docvecs['sports_%s' %(cnt4)]
        #print('%s' %(spo_vec))
        all_list.append(spo_vec)
        all_label_vec.append(4)
        cnt4 += 1

    #print(all_list)
    #print(all_label_vec)
    
    
    ####### Evaluation: Precision, Recall, F-score ########
    data_train = all_list
    label_train = all_label_vec
    estimator = SVC()

    data_train_s, data_test_s, label_train_s, label_test_s = train_test_split(data_train, label_train, test_size=0.4)
    estimator.fit(data_train_s, label_train_s)
    actual, predicted = label_test_s, estimator.predict(data_test_s)
    target = ['economic','entertainment','foreign','it','sports']
    y_true, y_pred = label_test_s, estimator.predict(data_test_s)
    print (metrics.classification_report(actual, predicted, target_names=target))
    