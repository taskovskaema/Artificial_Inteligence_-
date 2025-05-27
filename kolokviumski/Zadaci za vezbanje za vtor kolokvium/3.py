import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder

if __name__=='__main__':
    encoder=OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    iks=int(input())
    kriterium=input()
    # print(iks)

    obraten_iks=100-iks
    # print(obraten_iks/100)

    train_set=dataset[int((obraten_iks/100)*len(dataset)):]
    test_set= dataset[:int((obraten_iks/100)*len(dataset))]

    train_x=[row[:-1] for row in train_set]
    train_y=[row[-1] for row in train_set]

    train_x=encoder.transform(train_x)

    test_x=[row[:-1] for row in test_set]
    test_y=[row[-1] for row in test_set]

    test_x=encoder.transform(test_x)

    klasifikator=DecisionTreeClassifier(criterion=kriterium,random_state=0)
    klasifikator.fit(train_x,train_y)


# dlabocina
    print("Depth: "+str(klasifikator.get_depth()))

# br lisja
    print("Number of leaves: " + str(klasifikator.get_n_leaves()))

# tocnost
    tocnost=klasifikator.score(test_x,test_y)
    print("Accuracy: " + str(tocnost))
    # tocnost=0    #drug nachin
    # for i in range(len(test_set)):
    #     predict=klasifikator.predict([test_x[i]])[0]
    #
    #     if predict==test_y[i]:
    #         tocnost+=1
    #
    # print("Accuracy: " + str(tocnost/len(test_set)))


# najgolema karakteristika
    karakteristiki= list(klasifikator.feature_importances_)
    print("Most important feature: "+ str(karakteristiki.index(max(karakteristiki))))

# najmala karakteristika
    print("Least important feature: " + str(karakteristiki.index(min(karakteristiki))))




