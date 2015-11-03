from __future__ import division
from math import log
import numpy as np


#returns the number of x attributes with the given value and column number,rows are optional
def getXCountFromColumn(voting_data,colno,value,rows):
    if rows is None:
        return (sum(voting_data[:,colno]==value))
    else:
        return (sum(voting_data[rows,colno]==value))

#returns the number of Y's  present with the given value, rows are optional
def getYCount(value,rows):
    if rows is None:
        return sum(voting_data[:,0]==value)
    else:
        return sum(voting_data[rows,0]==value)

#get the missing rows for a particular column
def getMissingRows(voting_data,column):
    return np.where(voting_data[:,column]=='?')

#get the known rows for a particular column
def rowsknown(voting_data,column):
    rows=[];
    unknown_rows=getMissingRows(voting_data,column)
    for i in range(voting_data.shape[0]):
        if i not in unknown_rows:
            rows.append(i)
    return (rows)



# gives the probability of x given y for a given column
def probXGivenY(x,y,column,voting_data):


    unknown_indices=getMissingRows(voting_data,column)
    known_indices=rowsknown(voting_data,column)

    #getting indexes in attribute array which has the corresponding lable as y
    x_row=[]
    for i in known_indices:
        if voting_data[i,0]==y:
            x_row.append(i)

    #probability of x for known indices
    prob_x=[]
    prob_x[0]=getXCountFromColumn(voting_data,column,'0',known_indices)/len(known_indices)
    prob_x[1]=getXCountFromColumn(voting_data,column,'1',known_indices)/len(known_indices)

    probability=0
    for indices in unknown_indices:
        for value in ['1','0']:
             #case where the value of unkown index is equal to x and corresponding y value is equal to given value
            if value==x and voting_data[indices,0]==y:
                probability+= ((getXCountFromColumn(voting_data,column,x,x_row)+1)/(len(known_indices)+1))*prob_x[ord(value)]
            else:
                probability+=((getXCountFromColumn(voting_data,column,x,x_row))/(len(known_indices)+1))*prob_x[ord(value)]

    return probability




if __name__ == '__main__':

    voting_train_data=np.loadtxt('voting_train.data',delimiter=",",dtype=str)

    probability=np.zeros(((voting_train_data.shape[1],2,2)))
    for col in range(1,voting_train_data.shape[1]):
        for classifier in ['1','0']:
            for xvalue in ['1','0']:
                probability[col][ord(classifier)][ord(xvalue)]=probXGivenY(xvalue,classifier,col,voting_train_data)


    voting_test_data=np.loadtxt('voting_test.data',delimiter=",",dtype=str)
