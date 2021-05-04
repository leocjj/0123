#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder, OrdinalEncoder, LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, matthews_corrcoef, confusion_matrix
# explicitly require this experimental feature
from sklearn.experimental import enable_hist_gradient_boosting  # noqa
# now you can import normally from ensemble
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import RadiusNeighborsClassifier, KNeighborsClassifier
import seaborn as sns
import matplotlib.pyplot as plt
Deep = __import__('26-deep_neural_network').DeepNeuralNetwork

class Preprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.age = Pipeline(
            [("scale", MinMaxScaler()),
            ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True))]
        )
        self.fnlwgt = Pipeline(
            [("scale", MinMaxScaler()),
             ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True))]
        )
        self.education_num = Pipeline(
            [("scale", MinMaxScaler()),
             ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True))]
        )
        self.capital_net = Pipeline(
            [("scale", MinMaxScaler()),
             ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True))]
        )
        self.hours_per_week = Pipeline(
            [("scale", MinMaxScaler()),
             ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True))]
        )
        self.workclass = Pipeline(
            [("encode", OrdinalEncoder(dtype=np.int)),
            ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True)),
            ("scale", MinMaxScaler())]
        )
        self.marital_status = Pipeline(
            [("encode", OrdinalEncoder(dtype=np.int)),
            ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True)),
            ("scale", MinMaxScaler())]
        )
        self.occupation = Pipeline(
            [("encode", OrdinalEncoder(dtype=np.int)),
            ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True)),
            ("scale", MinMaxScaler())]
        )
        self.relationship = Pipeline(
            [("encode", OrdinalEncoder(dtype=np.int)),
            ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True)),
            ("scale", MinMaxScaler())]
        )
        self.race = Pipeline(
            [("encode", OrdinalEncoder(dtype=np.int)),
             ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True)),
             ("scale", MinMaxScaler())]
        )
        self.sex = Pipeline(
            [("encode", OrdinalEncoder(dtype=np.int)),
             ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True)),
             ("scale", MinMaxScaler())]
        )
        self.native_country = Pipeline(
            [("encode", OrdinalEncoder(dtype=np.int)),
             ("input", SimpleImputer(strategy="constant", fill_value=-1, add_indicator=True)),
             ("scale", MinMaxScaler())]
        )
        #self.hours_per_week = LabelEncoder()
        # dataset['Sex'] = dataset['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
        # dataset.loc[dataset['Fare'] <= 7.91, 'Fare'] = 0
        # dataset['Fare'] = dataset['Fare'].astype(int)

    def fit(self, X: pd.DataFrame, y=None):
        self.age.fit(X[["age"]])
        self.fnlwgt.fit(X[["fnlwgt"]])
        self.education_num.fit(X[["education-num"]])
        self.capital_net.fit(X[["capital-net"]])
        self.hours_per_week.fit(X[["hours-per-week"]])

        self.workclass.fit(X[["workclass"]])
        self.marital_status.fit(X[["marital-status"]])
        self.occupation.fit(X[["occupation"]])
        self.relationship.fit(X[["relationship"]])
        self.race.fit(X[["race"]])
        self.sex.fit(X[["sex"]])
        self.native_country.fit(X[["native-country"]])
        return self

    def transform(self, X: pd.DataFrame, y=None):
        features = [
            self.age.transform(X[["age"]])[:, 0],
            self.fnlwgt.transform(X[["fnlwgt"]])[:, 0],
            self.education_num.transform(X[["education-num"]])[:, 0],
            self.capital_net.transform(X[["capital-net"]])[:, 0],
            self.hours_per_week.transform(X[["hours-per-week"]])[:, 0],

            self.workclass.transform(X[["workclass"]])[:, 0],
            self.marital_status.transform(X[["marital-status"]])[:, 0],
            self.occupation.transform(X[["occupation"]])[:, 0],
            self.relationship.transform(X[["relationship"]])[:, 0],
            self.race.transform(X[["race"]])[:, 0],
            self.sex.transform(X[["sex"]])[:, 0],
            self.native_country.transform(X[["native-country"]])[:, 0]
            #self.Pclass.transform(X["Pclass"]),
            #np.array(X['Cabin']),
        ]
        return np.stack(features, axis=1)

def main():
    EXPORT = True
    train_size = 0.8 if not EXPORT else 1

    df = pd.read_csv("train.csv")
    # Unknow information
    #df.loc[df['workclass'] == ' ?', 'workclass'] = pd.NA
    #df.loc[df['occupation'] == ' ?', 'occupation'] = pd.NA
    #df.loc[df['native-country'] == ' ?', 'native-country'] = pd.NA
    #df[df['workclass'] == '?'] = pd.NA
    #df['workclass'].fillna(pd.NA, inplace=True)
    #df['Embarked'].fillna('C', inplace=True)
    #df['Age'].fillna(-1, inplace=True)

    test = pd.read_csv('test.csv')
    # Unknow information
    #df.loc[df['workclass'] == ' ?', 'workclass'] = ''
    #df.loc[df['occupation'] == ' ?', 'occupation'] = ''
    #df.loc[df['native-country'] == ' ?', 'native-country'] = ''

    df_train, df_valid = train_test_split(df, train_size=train_size, random_state=49)\
        if not EXPORT else (df, df)

    preprocessor = Preprocessor()
    preprocessor.fit(df_train)

    x_train = preprocessor.transform(df_train)
    y_train = df_train["target"]

    x_valid = preprocessor.transform(df_valid) if not EXPORT else None
    y_valid = df_valid["target"] if not EXPORT else None

    x_test = preprocessor.transform(test)

    # Tell us is that there are not too many features strongly correlated with one another.
    # Not correlated is good because this means that there isn't much redundant or superfluous data.
    # Disapear when the program finish.
    plt.figure(figsize=(14, 12))
    plt.title('Pearson Correlation of Features', y=1.05, size=15)
    sns.heatmap(pd.DataFrame(x_test.astype(float)).corr(), linewidths=0.1, vmax=1.0,
                square=True, cmap=plt.cm.get_cmap('RdBu'), linecolor='white', annot=True)

    #model = RandomForestClassifier(n_estimators=200, bootstrap=False, min_samples_split=49, criterion='entropy')     #78.81 ... 86.19
    #model = GradientBoostingClassifier(n_estimators=500, learning_rate=0.1, max_depth=5, random_state=0, verbose=True)   #77.08 ... 86.55
    #model = HistGradientBoostingClassifier(loss='binary_crossentropy', tol=1e-12, max_iter=10000, min_samples_leaf=2, verbose=True)          #78.87 ... 86.85
    model = MLPClassifier(hidden_layer_sizes=100, activation='tanh', solver='lbfgs', tol=1e-12, learning_rate='adaptive', verbose=True, max_iter=3790, random_state=1) #100    78.92 79.11 81.24 81.85 81.74 .. 84.03

    #GridSearchCV
    # Going to use these 5 base models for the stacking
    # from sklearn.ensemble import (RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, ExtraTreesClassifier)
    # from sklearn.svm import SVC

    #model = DecisionTreeClassifier(max_depth=None, min_samples_split=10, random_state = 0)                #78.56 ... 82.26
    #model = LogisticRegression(max_iter=1000, random_state=0)                                             #77.96 ... 81.83 ...
    #model = LogisticRegressionCV(max_iter=1000, random_state=0)                                           #78.016 ... 82.03
    #model = RadiusNeighborsClassifier(radius=9)                                                           #75.87 ... 75.87
    #model = KNeighborsClassifier(n_neighbors=6)                                                           #73.795 ... 81.76
    #model = GaussianNB()                                                                                  #78.667
    model.fit(x_train, y_train)

    if EXPORT:
        y_test_pred = model.predict(x_test)
        result = pd.DataFrame(np.stack((np.array(test['Id']), y_test_pred), axis=1), columns=['Id', 'Predicted'])
        result.to_csv('submission2.csv', index=False)
        print("Result exported.")
    else:
        y_valid_pred = model.predict(x_valid)
        accuracy = accuracy_score(y_valid, y_valid_pred)
        # mcc = matthews_corrcoef(y_valid, y_valid_pred)
        #metrics = dict(accuracy=accuracy) ###############################################################
        #params = dict(min_samples_split=min_samples_split)
        print("Accuracy: {}".format(accuracy))
        # print("Mcc: {}".format(mcc))
        # tn, fp, fn, tp = confusion_matrix([0, 1, 0, 1], [1, 1, 1, 0]).ravel()

    #print("Train size: {} Random state: {} Accuracy: {}".format(i, j, accuracy))
    #best.append(accuracy)
    #print(max(best))

    pass


if __name__ == "__main__":
    main()
