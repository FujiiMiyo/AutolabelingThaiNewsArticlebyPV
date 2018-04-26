# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:27:00 2018


"""

from gensim import models
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score


if __name__ == '__main__':
    
    ####### Get data from CSV ########
    #economic = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/economic_test.csv')
    education = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/education_test.csv')
    entertainment = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/entertainment_test.csv')
    it = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/it_test.csv')
    sports = pd.read_csv('/Users/RIKO/AnacondaProject/Dailynews/sports_test.csv')
    all_pd = pd.concat([education,entertainment,it,sports],axis=1)
    print(all_pd.columns)
    
    ####### Load model ########
    model = models.doc2vec.Doc2Vec(alpha=0.025, min_alpha=0.025)  # use fixed learning rate
    model_loaded = models.doc2vec.Doc2Vec.load('model_dailynews1_deepcut_noeco_1500')
    model_loaded1 = models.doc2vec.Doc2Vec.load('model_dailynews1_eng')
    model_loaded2 = models.doc2vec.Doc2Vec.load('model_dailynews1_mm')
    model_loaded3 = models.doc2vec.Doc2Vec.load('model_dailynews1_newmm')
    
    ####### Create lists of labels and vectors ########
    all_label_vec = []
    all_list = []
    all_label_vec1 = []
    all_list1 = []
    all_label_vec2 = []
    all_list2 = []
    all_label_vec3 = []
    all_list3 = []
    
    '''cnt = 0
    for i in all_pd['economic'].values:
        eco_vec = model_loaded.docvecs['economic_%s' %(cnt)]
        eco_vec1 = model_loaded1.docvecs['economic_%s' %(cnt)]
        eco_vec2 = model_loaded2.docvecs['economic_%s' %(cnt)]
        eco_vec3 = model_loaded3.docvecs['economic_%s' %(cnt)]
        #print('%s' %(eco_vec))
        all_list.append(eco_vec)
        all_label_vec.append(0)
        all_list1.append(eco_vec1)
        all_label_vec1.append(0)
        all_list2.append(eco_vec2)
        all_label_vec2.append(0)
        all_list3.append(eco_vec3)
        all_label_vec3.append(0)
        cnt += 1'''
        
    cnt1 = 0
    for i in all_pd['education'].values:
        edu_vec = model_loaded.docvecs['education_%s' %(cnt1)]
        edu_vec1 = model_loaded1.docvecs['education_%s' %(cnt1)]
        edu_vec2 = model_loaded2.docvecs['education_%s' %(cnt1)]
        edu_vec3 = model_loaded3.docvecs['education_%s' %(cnt1)]
        #print('%s' %(edu_vec))
        all_list.append(edu_vec)
        all_label_vec.append(0)
        all_list1.append(edu_vec1)
        all_label_vec1.append(0)
        all_list2.append(edu_vec2)
        all_label_vec2.append(0)
        all_list3.append(edu_vec3)
        all_label_vec3.append(0)
        cnt1 += 1
        
    cnt2 = 0
    for i in all_pd['entertainment'].values:
        ent_vec = model_loaded.docvecs['entertainment_%s' %(cnt2)]
        ent_vec1 = model_loaded1.docvecs['entertainment_%s' %(cnt2)]
        ent_vec2 = model_loaded2.docvecs['entertainment_%s' %(cnt2)]
        ent_vec3 = model_loaded3.docvecs['entertainment_%s' %(cnt2)]
        #print('%s' %(ent_vec))
        all_list.append(ent_vec)
        all_label_vec.append(1)
        all_list1.append(ent_vec1)
        all_label_vec1.append(1)
        all_list2.append(ent_vec2)
        all_label_vec2.append(1)
        all_list3.append(ent_vec3)
        all_label_vec3.append(1)
        cnt2 += 1  
        
    cnt3 = 0
    for i in all_pd['it'].values:
        it_vec = model_loaded.docvecs['it_%s' %(cnt3)]
        it_vec1 = model_loaded1.docvecs['it_%s' %(cnt3)]
        it_vec2 = model_loaded2.docvecs['it_%s' %(cnt3)]
        it_vec3 = model_loaded3.docvecs['it_%s' %(cnt3)]
        #print('%s' %(it_vec))
        all_list.append(it_vec)
        all_label_vec.append(2)
        all_list1.append(it_vec1)
        all_label_vec1.append(2)
        all_list2.append(it_vec2)
        all_label_vec2.append(2)
        all_list3.append(it_vec3)
        all_label_vec3.append(2)
        cnt3 += 1
        
    cnt4 = 0
    for i in all_pd['sports'].values:
        spo_vec = model_loaded.docvecs['sports_%s' %(cnt4)]
        spo_vec1 = model_loaded1.docvecs['sports_%s' %(cnt4)]
        spo_vec2 = model_loaded2.docvecs['sports_%s' %(cnt4)]
        spo_vec3 = model_loaded3.docvecs['sports_%s' %(cnt4)]
        #print('%s' %(spo_vec))
        all_list.append(spo_vec)
        all_label_vec.append(3)
        all_list1.append(spo_vec1)
        all_label_vec1.append(3)
        all_list2.append(spo_vec2)
        all_label_vec2.append(3)
        all_list3.append(spo_vec3)
        all_label_vec3.append(3)
        cnt4 += 1

    #print(all_list)
    #print(all_label_vec)
    
    
    ####### Evaluation: Precision, Recall, F-score ########
    data_train = all_list
    label_train = all_label_vec
    data_train1 = all_list1
    label_train1 = all_label_vec1
    data_train2 = all_list2
    label_train2 = all_label_vec2
    data_train3 = all_list3
    label_train3 = all_label_vec3
    estimator = SVC()
    
    
        ######### Deepcut ##########
    data_train_s, data_test_s, label_train_s, label_test_s = train_test_split(data_train, label_train, test_size=0.2)
    estimator.fit(data_train_s, label_train_s)
    actual, predicted = label_test_s, estimator.predict(data_test_s)
    target = ['education','entertainment','it','sports']
    y_true, y_pred = label_test_s, estimator.predict(data_test_s)
    print (metrics.classification_report(actual, predicted, target_names=target))
    #print(precision_recall_fscore_support(actual, y_pred, average='micro'))
    print(accuracy_score(actual, predicted))
    
    
        ######### Eng ##########
    '''data_train_s1, data_test_s1, label_train_s1, label_test_s1 = train_test_split(data_train1, label_train1, test_size=0.2, random_state=900)
    estimator.fit(data_train_s1, label_train_s1)
    actual1, predicted1 = label_test_s1, estimator.predict(data_test_s1)
    target1 = ['economic','education','entertainment','it','sports']
    y_true1, y_pred1 = label_test_s1, estimator.predict(data_test_s1)
    print (metrics.classification_report(actual1, predicted1, target_names=target1))
    
        ######### MM ##########
    data_train_s2, data_test_s2, label_train_s2, label_test_s2 = train_test_split(data_train2, label_train2, test_size=0.2, random_state=900)
    estimator.fit(data_train_s2, label_train_s2)
    actual2, predicted2 = label_test_s2, estimator.predict(data_test_s2)
    target2 = ['economic','education','entertainment','it','sports']
    y_true2, y_pred2 = label_test_s2, estimator.predict(data_test_s2)
    print (metrics.classification_report(actual2, predicted2, target_names=target2))
    
        ######### MM ##########
    data_train_s3, data_test_s3, label_train_s3, label_test_s3 = train_test_split(data_train3, label_train3, test_size=0.2, random_state=900)
    estimator.fit(data_train_s3, label_train_s3)
    actual3, predicted3 = label_test_s3, estimator.predict(data_test_s3)
    target3 = ['economic','education','entertainment','it','sports']
    y_true3, y_pred3 = label_test_s3, estimator.predict(data_test_s3)
    print (metrics.classification_report(actual3, predicted3, target_names=target2))
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    