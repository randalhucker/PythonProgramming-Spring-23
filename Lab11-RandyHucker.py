import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from pandas import DataFrame, Series
from sklearn import metrics

# Discussion:
#
# After analyzing the results, it is evident that the best estimators 
# for predicting housing prices in California are those that have R2 
# values close to 1.0 and MSE values close to 0. Multiple linear regression 
# yielded better scores on average than any single feature. However, Feature 1 (0) 
# was found to be the most accurate individual estimator, with an R2 score of 0.46 
# and an MSE score of 0.719, which were relatively close to the scores generated 
# by the multiple linear regression model (R2 of 0.6, MSE of 0.535). Therefore, 
# Feature 1 (0) is the most precise individual estimator for predicting housing 
# prices in California.

# In contrast, for all other individual features, the MSE values ranged around 1.3, 
# with the third feature (2) having the lowest value (1.308) and the fourth feature (3) having the highest(1.3421). 
# Additionally, the R2 score for all the other features was less than 0.025, 
# with the fourth feature (3) and sixth (5) having negative values. 
# A close-to-zero or actual negative R2 value indicates that the model cannot generate 
# accurate predictions using the given data. Since all of the individual features 
# fall into this category and have similar MSE scores, we can conclude that models 
# generated by single linear regression for features 1 through 7 are inadequate 
# estimators of California housing prices.

cali = fetch_california_housing()

cali_df = pd.DataFrame(cali.data, columns=cali.feature_names)

cali_df['MedHouseValue'] = pd.Series(cali.target)

X_train, X_test, Y_train, Y_test = train_test_split(
    cali.data, cali.target, random_state=11)

regress = LinearRegression()
regress.fit(X=X_train, y=Y_train)

predicted = regress.predict(X_test)
expected = Y_test
print("Multiple Linear Regression using All features:")
print(f"R2 Score: {metrics.r2_score(expected, predicted)}")
print(f"MSE Score: {metrics.mean_squared_error(expected, predicted)} \n")

e = enumerate(cali.feature_names)
for i, name in e:
    X_train, X_test, Y_train, Y_test = train_test_split(
        cali_df.iloc[:, i].values.reshape(-1, 1), cali.target, random_state=11)
    regress.fit(X=X_train, y=Y_train)
    predicted = regress.predict(X_test)
    expected = Y_test
    print(f'{"Feature " + str(i):>10} has R2 Score: {metrics.r2_score(expected, predicted)}')
    print(f'{"":>10} has MSE Score: {metrics.mean_squared_error(expected, predicted)} \n')

# z = zip(predicted[::1000], expected[::1000])
# for p, e in z:
#     #print(f'predicted: {p:.2f}, expected: {e:.2f}')
#     print(f"R2 Score: {metrics.r2_score(e, p)}")
#     print(f"MSE Score: {metrics.mean_squared_error(e, p)}")

# df = pd.DataFrame()
# df['Expected'] = pd.Series(expected)
# df['Predicted'] = pd.Series(predicted)
# figure = plt.figure(figsize=(9, 9))
# axes = sns.scatterplot(data=df,
#                        x='Expected', y='Predicted')
# start = min(expected.min(), predicted.min())
# end = max(expected.max(), predicted.max())
# axes.set_xlim(start, end)
# axes.set_ylim(start, end)
# line = plt.plot([start, end], [start, end],'k--')
