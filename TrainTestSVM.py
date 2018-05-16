import csv
import pandas as pd
from sklearn.svm import SVC
import itertools as it
from sklearn.ensemble import RandomForestClassifier
from math import sqrt

from sklearn import tree
import numpy as np


def getname():
    file = open("t-tested.csv", 'r')
    file2 = open("0-6.csv", 'r')


    nameProbe = []
    topProbes = []

    line = file.readline()
    line2 = file2.readline()



    i =0
    while i < 100:
        topProbes.append(int(line.split(',')[0]))
        line = file.readline()
        i+=1


    reader = csv.reader(file2)

    topProbes.sort()

    i = 0
    j = 0
    for row in reader:
        if i > int(topProbes[-1]):
            break
        #line2 = file2.readline().split('\t')
        name =row[0].split('\t')[1]

        if i == (int(topProbes[j])):
            nameProbe.append(name)
            j += 1
        i += 1



    output = open("nameTOP100.txt", 'w')

    for elem in nameProbe:
        output.write(elem+'\n')




def defineTrainTestSet():

    file = open("top100.csv", 'r')

    reader = csv.reader(file)

    i =0
    for row in reader:
        if i == 0:
            sampleTrain0 = row[1:155]
            sampleTest0 = row[155:207]

            sampleTrain6 = row[208:362]
            sampleTest6 = row[362:414]

            break


    file.close()

def createTrainSet():
    file = open("top100.csv", 'r')

    #reader = csv.reader(file)

    #traintest(5)


    print(max(traintest(20)))
    print("fin")
    print(max(traintest(10)))
    print("fin")
    print(max(traintest(5)))
    print("fin")

    print(max(traintest(4)))

    print("fin")
    print(max(traintest(2)))
    print("fin")
    print(max(traintest(1)))
    print("fin")





def traintest(n):
    '''
    combi = []
    df = pd.read_csv("top100.csv")

    for i in range(155):
        combi.append(i)

    c = it.combinations(combi,n)


    for combinations in c:
        X = []
        y = []
        test = []
        yTest = []



    '''
    results = []

    for mouad in range(0,n):


        X = []
        y = []
        test = []
        yTest = []

        i = 0

        df = pd.read_csv("top100.csv")

        nb_probe = int(100/n)
        debut= mouad*nb_probe

        fin = debut+nb_probe


        for column in df:
            tmp = []

            if i > 155 and i < 207: # test 0
                for j in range(debut,fin):
                    tmp.append(df[column][j])
                test.append(tmp)
                yTest.append(0)

            if 0 < i <= 155:
                for j in range(debut,fin): # train 0

                    tmp.append(df[column][j])
                X.append(tmp)
                y.append(0)

            if i > 207 and i < 362:
                for j in range(debut,fin): # train 0

                    tmp.append(df[column][j])
                X.append(tmp)
                y.append(1)

            if i > 362:
                for j in range(debut,fin):
                    tmp.append(df[column][j])
                test.append(tmp)
                yTest.append(1)



            i+=1

        clf = SVC()
        clf.fit(X, y)
        res = clf.predict(test)


        reussite = 0



        count = 0
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for i in range(len(yTest)):
            if res[i] == yTest[i]:
                count += 1

            if res[i] == 1 and yTest[i] == 1:
                tp += 1
            elif res[i] == 0 and yTest[i] == 0:
                tn += 1
            elif res[i] == 1 and yTest[i] == 0:
                fp += 1
            elif res[i] == 0 and yTest[i] == 1:
                fn += 1

        count = (count * 100) / len(res)

        print("reussite ", count)
        
        
        print("tp", tp)
        print("tn", tn)
        print("fp", fp)
        print("fn", fn)

        mcc = ((tp * tn) - (fp * fn)) / sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        print('mcc', mcc)
        presicion = tp / (tp + fp)
        print('precision : ', presicion)
        recall = tp / (fn + tp)
        print('recall:', recall)


        results.append(count)
        print("\n\n")
        return results










global sampleTrain0
global sampleTest0

global sampleTrain6
global sampleTest6

defineTrainTestSet()

createTrainSet()

