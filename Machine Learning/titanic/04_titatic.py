#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder, LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
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

class Preprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.age = Pipeline(
            [("scale", MinMaxScaler()),
            ("input", SimpleImputer(strategy="constant", fill_value=-1))]
        )
        # dataset['Sex'] = dataset['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
        # dataset.loc[dataset['Fare'] <= 7.91, 'Fare'] = 0
        # dataset['Fare'] = dataset['Fare'].astype(int)
        self.sex = LabelEncoder()
        self.Pclass = LabelEncoder()
        #self.Cabin = LabelEncoder()
        self.Parch = LabelEncoder()
        self.SibSp = LabelEncoder()
        self.Fare = LabelEncoder()
        self.Embarked = LabelEncoder()

    def fit(self, X: pd.DataFrame, y=None):
        self.age.fit(X[["Age"]])
        self.sex.fit(X["Sex"])
        self.Pclass.fit(X["Pclass"])
        #self.Cabin.fit(X["Cabin"])
        self.Parch.fit(X["Parch"])
        self.SibSp.fit(X["SibSp"])
        self.Fare.fit(X["Fare"])
        self.Embarked.fit(X["Embarked"])
        return self
    def transform(self, X: pd.DataFrame, y=None):
        features = [
            self.age.transform(X[["Age"]])[:, 0],
            self.sex.transform(X["Sex"]),
            self.Pclass.transform(X["Pclass"]),
            #np.array(X['Cabin']),
            np.array(X['Parch']),
            np.array(X["SibSp"]),
            np.array(X["Fare"]),
            self.Embarked.transform(X["Embarked"])
        ]
        return np.stack(features, axis=1)

def main():
    EXPORT = False
    random_state = 49
    train_size = 0.8 if not EXPORT else 1

    df = pd.read_csv("train.csv")
    df['Fare'].fillna(-1, inplace=True)
    df['Embarked'].fillna('C', inplace=True)
    df['Age'].fillna(-1, inplace=True)

    test = pd.read_csv('test.csv')
    test['Fare'].fillna(-1, inplace=True)
    test['Embarked'].fillna('C', inplace=True)
    test['Age'].fillna(-1, inplace=True)
    #df_train: pd.DataFrame
    #df_valid: pd.DataFrame
    df_train, df_valid = train_test_split(df, train_size=train_size, random_state=random_state) if not EXPORT else (
    df, df)

    preprocessor = Preprocessor()
    preprocessor.fit(df_train)

    x_train = preprocessor.transform(df_train)
    y_train = df_train["Survived"]

    x_valid = preprocessor.transform(df_valid) if not EXPORT else None
    y_valid = df_valid["Survived"] if not EXPORT else None

    x_test = preprocessor.transform(test)

    # Tell us is that there are not too many features strongly correlated with one another.
    # Not correlated is good because this means that there isn't much redundant or superfluous data.
    # Disapear when the program finish.
    plt.figure(figsize=(14, 12))
    plt.title('Pearson Correlation of Features', y=1.05, size=15)

    sns.heatmap(pd.DataFrame(x_test.astype(float)).corr(), linewidths=0.1, vmax=1.0,
                square=True, cmap=plt.cm.get_cmap('RdBu'), linecolor='white', annot=True)

    # model = RandomForestClassifier(min_samples_split=49)
    # model = DecisionTreeClassifier(max_depth=None, min_samples_split=10, random_state = 0)
    #for n in range(10, 200, 10):
    #    for l in range(1, 11, 1):
    #        for i in range(1, 100):
    #model = GradientBoostingClassifier(n_estimators=10, learning_rate=0.1, max_depth=5, random_state=0)
    #model = LogisticRegression(max_iter=1000, random_state=0)
    #model = LogisticRegressionCV(max_iter=1000, random_state=0)

    #model = MLPClassifier(hidden_layer_sizes=10, activation='tanh', max_iter=500, random_state=0) #100
    #model = RadiusNeighborsClassifier(radius=9)
    #model = KNeighborsClassifier(n_neighbors=3)
    #model = HistGradientBoostingClassifier(loss='binary_crossentropy', max_depth=4) # TEST WITH PD INSTEAD OF x_train
    model = GaussianNB()
    model.fit(x_train, y_train)

    if EXPORT:
        y_test_pred = model.predict(x_test)
        result = pd.DataFrame(np.stack((np.array(test['PassengerId']), y_test_pred), axis=1), columns=['PassengerId', 'Survived'])
        result.to_csv('gender_submission.csv', index=False)
        print("Result exported.")
    else:
        y_valid_pred = model.predict(x_valid)
        accuracy = accuracy_score(y_valid, y_valid_pred)
        metrics = dict(accuracy=accuracy)
        #params = dict(min_samples_split=min_samples_split)
        print("Metrics: {}".format(metrics))
        #print("Params: {}".format(params))

    #print("Train size: {} Random state: {} Accuracy: {}".format(i, j, accuracy))
    #best.append(accuracy)
    #print(max(best))

    pass



if __name__ == "__main__":
    main()
