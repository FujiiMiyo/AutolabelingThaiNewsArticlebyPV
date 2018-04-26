# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 00:36:03 2018


"""

from gensim import models
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
import pandas as pd


if __name__ == '__main__':
    
    ####### Get data from CSV ########
    entertainment = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/entertainment.csv')
    it = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/it.csv')
    all_pd = pd.concat([entertainment,it],axis=1)
    print(all_pd.columns)
    
    ####### Load model ########
    model = models.doc2vec.Doc2Vec(alpha=0.025, min_alpha=0.025)  # use fixed learning rate
    model_loaded = models.doc2vec.Doc2Vec.load('model_dailynews_deepcut')
    
    ####### Create lists of labels and vectors ########
    cnt = 0
    all_label_vec = []
    all_list = []
    for i in all_pd['entertainment'].values:
        ent_vec = model_loaded.docvecs['entertainment_%s' %(cnt)]
        #print('%s' %(ent_vec))
        all_list.append(ent_vec)
        all_label_vec.append(0)
        cnt += 1
        
    cnt1 = 0
    for i in all_pd['it'].values:
        if i is not 'nan':
            it_vec = model_loaded.docvecs['it_%s' %(cnt1)]
            #print('%s' %(it_vec))
            all_list.append(it_vec)
            all_label_vec.append(1)
            cnt1 += 1

    print(all_list)
    print(all_label_vec)
    
    
    ####### Evaluation: Precision, Recall, F-score ########
    data_train = all_list
    label_train = all_label_vec
    estimator = SVC()

    data_train_s, data_test_s, label_train_s, label_test_s = train_test_split(data_train, label_train, test_size=0.2)
    estimator.fit(data_train_s, label_train_s)
    actual, predicted = label_test_s, estimator.predict(data_test_s)
    target = ['entertainment','it']
    y_true, y_pred = label_test_s, estimator.predict(data_test_s)
    print (metrics.classification_report(actual, predicted, target_names=target))
    