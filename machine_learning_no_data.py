#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 23:19:56 2017

@author: vishaalbommena
"""
import numpy as np
from random import randint
from sklearn.naive_bayes import GaussianNB
from operator import itemgetter


clf = GaussianNB()

def run_avg(X, a):
    y = []
    size = len(X)
    for i in range(0, size):
        y.append(a)
    return y


def ml_train_no(X):
    train = []
    train_1 = []
    train_2 = []
    for i in range (len(X)):
        if (i < (len(X) / 2)):
            train_1.append(X[i])
        else: 
            train_2.append(X[i])
    train = train_1 + train_2
    #train.append(train_temp)
    y1 = run_avg(train_1, 0)
    y2 = run_avg(train_2, 1)
    y = y1 + y2
    clf.fit(np.array(train).reshape(-1, 1), np.array(y))
    print("Training Complete")

def ml_predict_no(X, names):
    Y = clf.predict_proba(np.array(X).reshape(-1, 1))
    fin_list = []
    for i in range(0, len(Y)):
        temp = []
        temp.append(names[i][0])
        temp.append(Y[i][0])
        fin_list.append(temp)
    Y = sorted(fin_list, key=itemgetter(1))
    names = []
    preds = []
    for i in range(0, len(Y)):
        names.append(Y[i][0])
        preds.append(Y[i][1])
    return names, preds