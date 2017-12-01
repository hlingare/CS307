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
        if (int(Y[i])) == 11:
            for j in range(0, len(X[i])):
                X[i][j] = X[i][j] - 10
        if (int(Y[i])) == 12:
            for j in range(0, len(X[i])):
                X[i][j] = X[i][j]
        if (int(Y[i])) == 13:
            for j in range(0, len(X[i])):
                X[i][j] = X[i][j] + 10
    return X

def ml_train(X, clf):
    clf.fit(X)
    print("Training Complete")

def ml_distances(X,clf):
    distances, indexes = clf.kneighbors(X)
    for i in range(0,len(X)):
        X[i].append(distances[i][0])
    #distances = X
    distance = list(sorted(X,key=itemgetter(5)))
    print(distance)
    return distance

def run_avg(X, a):
    y = []
    size = len(X)
    for i in range(0, size):
        y.append(a)
    return y
