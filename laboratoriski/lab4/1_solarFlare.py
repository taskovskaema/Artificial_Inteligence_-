//DECISION TREES

import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder

if __name__ == '__main__':
    # Vashiot kod tuka

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    x = int(input())
    kriterium = input()

    train_set = dataset[int((1 - x / 100.0) * len(dataset)):]
    test_set = dataset[:int((1 - x / 100.0) * len(dataset))]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    train_x = encoder.transform(train_x)

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    test_x = encoder.transform(test_x)

    klasifikator = DecisionTreeClassifier(criterion=kriterium, random_state=0)
    klasifikator.fit(train_x, train_y)

    print("Depth: ", end='')
    print(klasifikator.get_depth())

    print("Number of leaves: ", end='')
    print(klasifikator.get_n_leaves())

    tocni = 0

    for i in range(len(test_set)):

        predict = klasifikator.predict([test_x[i]])[0]

        if predict == test_y[i]:
            tocni = tocni + 1

    print("Accuracy: ", end='')
    print(tocni / len(test_set))

    vazhni = list(klasifikator.feature_importances_)

    print("Most important feature: ", end='')
    print(vazhni.index(max(vazhni)))

    print("Least important feature: ", end='')
    print(vazhni.index(min(vazhni)))

    submit_train_data(train_x, train_y)

    submit_test_data(test_x, test_y)

    submit_classifier(klasifikator)

    submit_encoder(encoder)
