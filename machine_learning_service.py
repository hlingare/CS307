# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:23:47 2017

@author: Vishaal Bommena
"""
import numpy as np
from random import randint
from sklearn import neighbors
from operator import itemgetter

def normalize(X, Y):
    for i in range (0, len(Y)):
        if (Y[i]) == 11:
            for j in range(0, len(X[i])):
                X[i][j] = X[i][j] - 4
        if (Y[i]) == 12:
            for j in range(0, len(X[i])):
                X[i][j] = X[i][j] - 2
        if (Y[i]) == 13:
            for j in range(0, len(X[i])):
                X[i][j] = X[i][j] - 0
    return X

def ml_train(X, clf):
    #X = normalize(X, option)
    #Training Session
    print("clf: ", clf)
    y= []
    train = []
    X1 = []
    X2 = []
    for i in range (0, len(X)):
        if (i < (len(X) / 2)):
            X1.append(X[i])
        else:
            X2.append(X[i])
    y_0 = run_avg(X1, 0)
    y_1 = run_avg(X2, 1)
    train = X1 + X2
    y=y_0 + y_1
    clf.fit(train, y)
    print("Training Complete")

def ml_distances(X,clf):
    print("prediction: ", X)
    distances, indexes = clf.kneighbors(X)
    for i in range(0,len(X)):
        X[i].append(distances[i][0])
    distances = sorted(X,key=itemgetter(5))
    print("distances: ", distances)
    return distances

def run_avg(X, a):
    y = []
    size = len(X)
    for i in range(0, size):
        y.append(a)
    return y
