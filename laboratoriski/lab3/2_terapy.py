import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sklearn.naive_bayes import GaussianNB
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'], 
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'], 
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka
    # print(dataset)
    dataset = [[float(i) for i in row] for row in dataset]

    train_test = dataset[:int(0.85 * len(dataset))]
    train_x = [row[:-1] for row in train_test]
    train_y = [row[-1] for row in train_test]

    test_set = dataset[int(0.85 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    accuracy = classifier.score(test_x, test_y)
    print(accuracy)

    input_test = list(map(float, input().split(" ")))
    prediction = classifier.predict([input_test])[0]
    print(int(prediction))
    print(classifier.predict_proba([input_test]))
    
    
    
    
"""
    Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    klasifikatorot i encoderot so povik na slednite funkcii
    
    submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)
    
    submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)
    
    submit na klasifikatorot
    submit_classifier(classifier)
    
    povtoren import na kraj / ne ja otstranuvajte ovaa linija
"""
