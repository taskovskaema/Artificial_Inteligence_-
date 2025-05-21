import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka
    
  
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.75 * len(dataset))]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    
    train_X = encoder.transform(train_X)

    test_set = dataset[int(0.75 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]
    
    test_X = encoder.transform(test_X)
    
    classifier = CategoricalNB()
    classifier.fit(train_X, train_Y)

    accuracy = classifier.score(test_X, test_Y)
    print(accuracy)

    input_predict = input().split(" ")
    input_predict = encoder.transform([input_predict])

    prediction = classifier.predict(input_predict)[0]
    print(prediction)
    pred_proba = classifier.predict_proba(input_predict)
    print(pred_proba)
    
    submit_train_data(train_X, train_Y)
    submit_test_data(test_X, test_Y)
    submit_classifier(classifier)
    submit_encoder(encoder)
