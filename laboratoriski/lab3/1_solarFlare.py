import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
# from submission_script import *
# from dataset_script import dataset

if __name__ == '__main__':
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])
    # konvertirajgi site podatoci sho ke gi koristis osven klasata
    # da gi enkodirame site  koj sakame da gi koristime

    # tuka vika prvite 75% za treniranje
    train_set = dataset[:int(0.75 * len(dataset))]
    # za ova vika ostanatite 25% za testiranje
    test_set = dataset[int(0.75 * len(dataset)):]

    # ja trenirame mashinata so site elementi od listitie osven posledniot element koj e klasa i tochen odgovor
    # ['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0']
    # |-----------------------X------------------------||-Y-|
    train_x = [row[:-1] for row in train_set]
    # tocniot odgovor koj treba so train_x da go dobie (Y)
    train_y = [row[-1] for row in train_set]

    train_x=encoder.transform(train_x)
    # poshto train_x podatocite ke mu trebat na mashinata da vezhba

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    test_x=encoder.transform(test_x)

    # klasifikatorot spored koj mashinata ke vezhba
    classifier = CategoricalNB()
    classifier.fit(train_x, train_y)

    tocnost = classifier.score(test_x, test_y)
    print(tocnost)

    # На влез се прима еден запис за кој треба да се направи предвидување на класата.
    # На излез треба да се испечати точноста на моделот, класата на предвидување
    # како и веројатностите за припадност во класите.

    # [H R X 1 2 1 1 2 1 1]
    test = input().split(" ")
    # enkodiraj gi i napraj gi vo lista da e ko dataseto
    test = encoder.transform([test])

    predviduvanje = classifier.predict(test)[0]  #If you input one sample, you'll still get a list with one value, e.g. ['0'].
                                                # Using [0] extracts that single prediction from the list.
    print(predviduvanje)
    predviduvanje2 = classifier.predict_proba(test)
    print(predviduvanje2)

# submit na trenirachkoto mnozestvo
# submit_train_data(train_X, train_Y)
# submit na testirachkoto mnozestvo
# submit_test_data(test_X, test_Y)
# submit na klasifikatorot
# submit_classifier(classifier)
# submit na encoderot
# submit_encoder(encoder)
