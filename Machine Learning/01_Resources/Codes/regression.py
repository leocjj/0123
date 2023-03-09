import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# rather than importing the whole sklearn library,
we will import certain modules
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
# we load the dataset and save it as the variable
boston
boston = load_boston()
# if we want to know what sort of detail is
provided with this dataset, we can call .keys()
boston.keys()
# the info at the .DESCR key will tell us more
print(boston.DESCR)
Ajit Jaokar – Dan Howarth
– 50 –
# we can use pandas to create a dataframe, which is
basically a way of storing and operating on tabular
data
# here we pass in both the data and the column
names as variables
boston_X = pd.DataFrame(boston.data, columns =
boston.feature_names)
# we can then look at the top of the dataframe to
see the sort of values it contains
boston_X.head()
# pandas has a lot of functionality to assist with
exploratory data analysis
# .describe() provide summary statistics on all
numeric columns
print(boston_X.describe())
# we can also see the shape of the data
print(boston_X.shape)
"""* For each feature, we can see the `count`, or
number of data entries, the `mean` value, and the
`standard deviation`, `min`, `max` and `quartile`
values.
* We can see that the range of values for each
feature differs quite a lot, so we can start to
think about whether to apply normalization to the
data.
* We can also see that the `CHAS` faeture is either
a `(1,0)` value. If we look back at our
description, we can see that this is an example of
a `categorical` variable. These are values used to
describe non-numeric data. In this case, a `1`
indicates the house borders near the river, and a
`0` that it doesn't.
"""
# we can build on this analysis by plotting the
distribution and boxplots for each column
# we loop through all the columns
for col in boston_X.columns:
Classification and Regression: In a Weekend – Appendix
– 51 –
# and for each column we create space for one
row with 2 charts
f, axes = plt.subplots(1, 2, figsize=(12, 6))
# our first chart is a histogram and we set the
title
boston_X[col].hist(bins = 30, ax = axes[0])
axes[0].set_title('Distribution of '+ col)
# our second column is the boxplot
boston_X.boxplot(column = col, ax = axes[1])
# we then use this to command to display the
charts
plt.show()
"""* A `histogram` tells is the number of times, or
frequency, a value occurs within a `bin`, or
bucket, that splits the data (and which we
defined). A histogram shows the frequency with
which values occur within each of these bins, and
can tell us about the distribution of data.
* A `boxplot` captures within the box the
`interquartile range`, the range of values from
Q1/25th percentile to Q3/75th percentile, and the
median value. It also captures the `min` and `max`
values of each feature.
* Together, these charts show us the distribution
of values for each feature. We can start to make
judgements about how to treat the data, for example
whether we want to deal with outliers; or whether
we want to normalize the data.
"""
# we can now look at our target variable
boston_y = boston.target
# we can plot a histogram in a slightly different
way
plt.hist(boston_y, bins = 40)
plt.title('Housing price distribution, $K')
plt.show()
# and the same for the boxplot
plt.boxplot(boston_y)
plt.title('Box plot for housing price.')
plt.show()
Ajit Jaokar – Dan Howarth
– 52 –
# another thing we can do is plot a boxplot of one
variable against the target variable
# it is interesting to see how house value
distribution differs by CHAS, the categorical
variable
# here we create a grouped dataframe that includes
the target variable
grouped_df = boston_X.copy() # note we create a
copy of the data here so that any changes don't
impact the original data
grouped_df['target'] = boston_y.copy()
# we then plot it here
f, axes = plt.subplots(1, 1, figsize=(10, 5))
grouped_df.boxplot(column='target', by = 'CHAS',
ax = axes)
plt.show()
"""* The `interquartile range`for houses next to
the river is higher than for those houses not next
to the river, and the `min` and `max` values differ
too.
* This suggests this could be an important variable
for us to include in our model, given that as it
differs, the target value distribution changes.
"""
# we can extend this sort of analysis by creating a
heatmap
# this shows the correlation between the features
and target
# first we compute the correlation
corr = grouped_df.corr(method='pearson')
# and plot our figure size
plt.figure(figsize = (15, 10))
# and use seaborn to fill this figure with a
heatmap
sns.heatmap(corr, annot = True)
Classification and Regression: In a Weekend – Appendix
– 53 –
"""* We will let you review this heatmap to see
what features are important for modelling and
why."""
# OPTIONAL: below is code that generate a pairplot
using seaborn
# look up what a pairplot is and see if you can
interpret the output of the code below
#sns.pairplot(grouped_df)
"""#### Preprocess the data
* We proprocess the data to ensure it is a suitable
state for modelling. The sort of things that we do
to preprocess the data includes:
* *Dealing with missing values*, where we
identify what, if, any missing data we have and how
to deal with it. For example, we may replace
missing values with the mean value for that
feature, or by the average of the neighbouring
values.
* `pandas` has a number of options for filling
in missing data that is worth exploring
* We can also use `k-nearest neighbour`to help
us predict what the missing values should be, or
`sklearn Imputer` function (amongst other ways)
* *Treat categorical values*, by converting them
into a numerical representation that can be
modelled.
* There are a number of different ways to do
this in `sklearn` and `pandas`
* *Normalise the data*, for example by ensuring
the data is, for example all on the scale (such as
within two defined values); normally distributed;
has a zero-mean, etc. This is sometimes necessary
for the ML models to work, and can also help speed
up the time it takes for the models to run.
* Again, `sklearn` and `pandas` have in-built
functions to help you do this.
* In this notebook, we will look to remove
`outliers`, which are values that might be
erroneous and which can over-influence the model,
and `normalize` the data
"""
Ajit Jaokar – Dan Howarth
– 54 –
# lets start by removing outliers
# here we define the columns where we have
identified there could be outliers
numeric_columns = ['CRIM', 'ZN', 'INDUS', 'NOX',
'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B',
'LSTAT']
# this function can be used on any dataset to
return a list of index values for the outliers
def get_outliers(data, columns):
# we create an empty list
outlier_idxs = []
for col in columns:
elements = data[col]
# we get the mean value for each column
mean = elements.mean()
# and the standard deviation of the column
sd = elements.std()
# we then get the index values of all
values higher or lower than the mean +/- 2 standard
deviations
outliers_mask = data[(data[col] > mean +
3*sd) | (data[col] < mean - 3*sd)].index
# and add those values to our list
outlier_idxs += [x for x in outliers_mask]
return list(set(outlier_idxs))
# we call the function we just created on the
boston dataset
boston_outliers = get_outliers(boston_X,
numeric_columns)
# and drop those values from our feature and target
values
boston_X = boston_X.drop(boston_outliers, axis = 0)
boston_y =
pd.DataFrame(boston_y).drop(boston_outliers, axis =
0).values.ravel()
# we can check that this code has worked by looking
at the shape of our data
print (boston_X.shape)
Classification and Regression: In a Weekend – Appendix
– 55 –
print (boston_y.shape)
# we can also create a function to normalize our
data
# first lets look at the data before normalisation
boston_X[0:10]
# this function loops through columns in a data set
and defines a predefined scaler to each
def scale_numeric(data, numeric_columns, scaler):
for col in numeric_columns:
data[col] =
scaler.fit_transform(data[col].values.reshape(-1,
1))
return data
# we can now define the scaler we want to use and
apply it to our dataset
# a good exercise would be to research waht
StandardScaler does - it is from the scikit learn
library
scaler = StandardScaler()
boston_X = scale_numeric(boston_X, numeric_columns,
scaler)
# here we can see the result
boston_X[0:10]
"""### : Split the data
* In order to train our model and see how well it
performs, we need to split our data into training
and testing sets.
* We can then train our model on the training set,
and test how well it has generalised to the data on
the test set.
* There are a number of options for how we can
split the data, and for what proportion of our
original data we set aside for the test set.
"""
# a common way for splitting our dataset is using
train_test_split
Ajit Jaokar – Dan Howarth
– 56 –
# as an exercise, go to the scikit learn
documentation to learn more about this function and
the parameters available
X_train, X_test, Y_train, Y_test =
model_selection.train_test_split(boston_X,
boston_y, test_size = 0.2, random_state = 5)
# get shape of test and training sets
print('Training Set:')
print('Number of datapoints: ', X_train.shape[0])
print('Number of features: ', X_train.shape[1])
print('\n')
print('Test Set:')
print('Number of datapoints: ', X_test.shape[0])
print('Number of features: ', X_test.shape[1])
"""### Choose a Baseline algorithm
# linear regression is a fairly simple algorithm
compared to more complicate regression options, so
provides a good baseline
lm = LinearRegression()
"""### Train and Test the Model"""
# fitting the model to the data means to train our
model on the data
# the fit function takes both the X and y variables
of the training data
lm.fit(X_train, Y_train)
# from this, we can generate a set of predictions
on our unseen features, X_test
Y_pred = lm.predict(X_test)
"""### : Choose an evaluation metric
* We then need to compare these predictions with
the actual result and measure them in some way.
* This is where the selection of evaluation metric
is important. For regression, we measure the
distance between the predicted and actual answers
in some way. The shorter the distance, the more
correct the model is.
* We cover three common metrics below:
Classification and Regression: In a Weekend – Appendix
– 57 –
* `Mean Absolute Error`: which provides a mean
score for all the predicted versus actual values as
an absolute value
* `Means Squared Error`: which provides a mean
score for all the predicted versus actual values as
a square of the absolute value
* `R2`: which we recommend you research as an
exercise to grow your knowledge. WIkipedia and
`sklearn` document are a great place to start!
"""
def evaluate(Y_test, Y_pred):
# this block of code returns all the metrics we
are interested in
mse = metrics.mean_squared_error(Y_test,
Y_pred)
msa = metrics.mean_absolute_error(Y_test,
Y_pred)
r2 = metrics.r2_score(Y_test, Y_pred)
print("Mean squared error: ", mse)
print("Mean absolute error: ", msa)
print("R^2 : ", r2)
# this creates a chart plotting predicted and
actual
plt.scatter(Y_test, Y_pred)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs
$\hat{Y}_i$")
evaluate(Y_test, Y_pred)
# we can explore how metrics are dervied in a
little more detail by looking at MAE
# here we will implement MAE using numpy, building
it up step by step
# with MAE, we get the absolute values of the error
- as you can see this is of the difference between
the actual and predicted values
np.abs(Y_test - Y_pred)
Ajit Jaokar – Dan Howarth
– 58 –
# we will then sum them up
np.sum(np.abs(Y_test - Y_pred))
# then divide by the total number of
predictions/actual values
# as you will see, we get to the same score
implemented above
np.sum(np.abs(Y_test - Y_pred))/len(Y_test)
"""### : Refine our dataset
* This step allows us to add or modify features of
the datatset. We might do this if, for example,
some combination of features better represents the
problems space and so is an indicator of the target
variable.
* Here, we create one additional feature as an
example, but you should reflect on our EDA earlier
and see whether there are other features that can
be added to our dataset.
"""
# here we are using pandas functionality to add a
new column called LSTAT_2, which will feature
values that are the square of LSTAT values
boston_X['LSTAT_2'] = boston_X['LSTAT'].map(lambda
x: x**2)
# we can run our train_test_split function and see
that we have an additional features
X_train, X_test, Y_train, Y_test =
model_selection.train_test_split(boston_X,
boston_y, test_size = 0.2, random_state = 5)
print('Number of features after dataset refinement:
', X_train.shape[1])
# we can now run the same code as before on our
refined dataset to see if things have improved
lm.fit(X_train, Y_train)
Y_pred = lm.predict(X_test)
evaluate(Y_test, Y_pred)
Classification and Regression: In a Weekend – Appendix
– 59 –
"""### Step 8: Test Alternative Models
* Once we got a nice baseline model working for
this dataset, we also can try something more
sophisticated and rather different, e.g.
RandomForest Regressor. So, let's do so and also
evaluate the result.
"""
# as you can see, its very similar code to
instantiate the model
# we are able to pass in additional parameters as
the model is created, so optionally you can view
the documentation and play with these values
rfr = RandomForestRegressor()
rfr.fit(X_train, Y_train)
Y_pred = rfr.predict(X_test)
evaluate(Y_test, Y_pred)
"""### : Choose the best model and optimise its
parameters
* We can see that we have improved our model as we
have added features and trained new models.
* At the point that we feel comfortable with a good
model, we can start to tune the parameters of the
model.
* There are a number of ways to do this, and a
common way is shown below
"""
## grid search is a 'brute force' search, one that
will explore every possible combination of
parameters that you provide it
# we first define the parameters we want to search
as a dictionary. Explore the documentation to what
other options are avaiable
params = {'n_estimators': [100, 200], 'max_depth' :
[2, 10, 20]}
# we then create a grid search object with our
chosen model and paramters. We also use cross
validation here - explored more in Day 2
Ajit Jaokar – Dan Howarth
– 60 –
grid = model_selection.GridSearchCV(rfr, params,
cv=5)
# we fit our model to the data as before
grid.fit(X_train, Y_train)
# one output of the grid search function is that we
can get the best_estimator - the model and
parameters that scored best on the training data -
# and save it as a new a model
best_model = grid.best_estimator_
# and use it to predict and evaluate as before
Y_pred = best_model.predict(X_test)
evaluate(Y_test, Y_pred)