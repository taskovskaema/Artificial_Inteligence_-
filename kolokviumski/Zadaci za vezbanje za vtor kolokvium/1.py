import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

//dataset
if __name__ == '__main__':
    encoder=OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set=dataset[:int(0.75*len(dataset))] # 75%
    test_set=dataset[int(0.75*len(dataset)):] # 25%

    train_x=[row[:-1] for row in train_set]
    train_y=[row[-1] for row in train_set]

    train_x=encoder.transform(train_x)

    test_x=([row[:-1] for row in test_set])
    test_y=([row[-1] for row in test_set])

    test_x=encoder.transform(test_x)

#   otkako ke gi sredime podatocite da se soodvetni za treniranje ke pocnime da go trenirame

    classifier=CategoricalNB()
    classifier.fit(train_x,train_y) #trenira

    tocnost=classifier.score(test_x,test_y)
    print(tocnost)

    test=input().split(" ")
    test=encoder.transform([test]) #+lista [ ]

    pretpostavka=classifier.predict(test)[0]
    print(pretpostavka)
    pretpostavka2=classifier.predict_proba(test)
    print(pretpostavka2)

