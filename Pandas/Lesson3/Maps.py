import pandas as pd

reviews = pd.read_csv("D:\Lam-Nhat-Tien\CODE\DS & AI\Pandas\Data_set\wine_review\winemag-data-130k-v2.csv",index_col=0)

# map()
# suppose we want to remean the scores the wine received to 0. We can do:
reviews_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - reviews_points_mean)

# apply()
# is an equivalent method to map() if we want to transform a whole DataFrame by calling a custom method on each row.
def remean_points(row):
    row.points = row.points - reviews_points_mean
    return row

reviews.apply(remean_points, axis='columns')

''' NOTE: 
        map() and apply() return new, transformed Series and DataFrames, respectively.
        They don't modify the original data they're called on.
'''

# here's a faster way of remeaning our points column:
reviews_points_mean = reviews.points.mean()
reviews.points - reviews_points_mean

# Pandas will also understand what to do if we perform these operations between series of equal length.
# For example, an easy way to combining country and region information in the data set :
reviews.country + "-" + reviews.region_1 

'''
These operators are faster than map() or apply() because they use speed ups built into pandas.
However, they are not as flexible as map() or apply(), which can do more advanced things, like applying conditional logic, which cannot be done with addition and subtraction alone.
'''