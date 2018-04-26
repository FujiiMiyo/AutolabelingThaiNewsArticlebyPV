# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 01:29:17 2018


"""


from gensim import models
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support


if __name__ == '__main__':
    
    ####### Get data from CSV ########
    economic = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/economic_test.csv')
    education = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/education_test.csv')
    entertainment = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/entertainment_test.csv')
    entertainment_test = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/entertainment_test.csv')
    it = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/it1.csv')
    it1 = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/it.csv')
    sports = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/sports1.csv')
    all_pd = pd.concat([entertainment,economic],axis=1)
    #print(all_pd.columns)
    
    ####### Load model ########
    model = models.doc2vec.Doc2Vec(alpha=0.025, min_alpha=0.025)  # use fixed learning rate
    model_loaded = models.doc2vec.Doc2Vec.load('model_dailynews1_deepcut_ec')
    model_loaded_test = models.doc2vec.Doc2Vec.load('model_dailynews_test_deepcut')
    
    
    ####### Create lists of labels and vectors ########
    all_label_vec = []
    all_list = []
    all_label_vec1 = []
    all_list1 = []
    
    cnt = 0
    for i in all_pd['entertainment'].values:
        eco_vec = model_loaded.docvecs['entertainment_%s' %(cnt)]
        #print('%s' %(eco_vec))
        all_list.append(eco_vec)
        all_label_vec.append(0)
        cnt += 1
        
    cnt1 = 0
    for i in all_pd['economic'].values:
        eco_vec = model_loaded.docvecs['economic_%s' %(cnt1)]
        #print('%s' %(eco_vec))
        all_list.append(eco_vec)
        all_label_vec.append(1)
        cnt1 += 1
         
    
    #print(all_list)
    #print(all_label_vec)
    
    
    ####### Evaluation: Precision, Recall, F-score ########
    data_train = all_list
    label_train = all_label_vec
    data_train1 = all_list1
    label_train1 = all_label_vec1
    estimator = SVC()
    
        ######### Deepcut ##########
    #data_train_s1, data_test_s1, label_train_s1, label_test_s1 = train_test_split(data_train1, label_train1, test_size=0.2, random_state=900)
    data_train_s, data_test_s, label_train_s, label_test_s = train_test_split(data_train, label_train, test_size=0.2, random_state=42)
    estimator.fit(data_train_s, label_train_s)
    actual, predicted = label_test_s, estimator.predict(data_test_s)
    target = ['entertainment','economic']
    y_true, y_pred = label_test_s, estimator.predict(data_test_s)
    print (metrics.classification_report(actual, predicted, target_names=target))