from __future__ import division
import numpy as np



def countXgivenY(x,y,column,voting_data):
    rows=voting_data.shape[0]
    count=0
    for i in range(rows):
        if voting_data[i,column]==x and voting_data[i,0]==y:
           count+=1
    return count


#returns the number of x attributes with the given value and column number,rows are optional
def getXCountFromColumn(voting_data,colno,value,rows):
    if rows is None:
        return (sum(voting_data[:,colno]==value))
    else:
        return (sum(voting_data[rows,colno]==value))


#get the missing rows for a particular column
def getMissingRows(voting_data,column):
    return np.where(voting_data[:,column]=='?')



def probXGivenYNew(x,y,column,voting_data):

    countKnownAttributes=voting_data.shape[0]-len(getMissingRows(voting_data,column))

    return countXgivenY(x,y,column,voting_data)/countKnownAttributes


def probXGivenYNew1(row,voting_data,probability,y):
    result=1
    for i in range(1,voting_data.shape[1]):
        if(voting_data[row,i]!='?'):
            x=ord(voting_data[row,i])-48
            result=result*probability[i,x,y]

    return result

if __name__ == '__main__':

    voting_train_data=np.loadtxt('mean_train.data',delimiter=",",dtype=str)

    probability=np.zeros(((voting_train_data.shape[1],2,2)))
    for col in range(1,voting_train_data.shape[1]):
        for classifier in ['1','0']:
            for xvalue in ['1','0']:
                probability[col,ord(xvalue)-48,ord(classifier)-48]=probXGivenYNew(xvalue,classifier,col,voting_train_data)

    probabilityYOne=sum(voting_train_data[:,0]=='1')/voting_train_data.shape[0]
    probabilityYZero=1-probabilityYOne



    voting_test_data=np.loadtxt('ignore_test.data',delimiter=",",dtype=str)

    label=[0 for i in range(voting_test_data.shape[0])]
    rows=voting_test_data.shape[0]
    for i in range(rows):
        if probabilityYOne*probXGivenYNew1(i,voting_test_data,probability,1)>probabilityYZero*probXGivenYNew1(i,voting_test_data,probability,0):
            label[i]='1'
        else:
            label[i]='0'

    count=0
    for i in range(voting_test_data.shape[0]):
        if label[i]==voting_test_data[i,0]:
           count+=1

    print "Accuracy="+str((count/voting_test_data.shape[0])*100)





