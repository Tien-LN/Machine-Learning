import pandas as pd

reviews = pd.read_csv("D:\Lam-Nhat-Tien\CODE\DS & AI\Pandas\Data_set/fifa_players.csv",index_col=0)
reviews

# we can check if each player is Portuguese or not
reviews.nationality == "Portugal"

#This result can then be used inside of loc to select the relevant data:
reviews.loc[reviews.nationality == "Portugal"]

#We can use the ampersand (&) to bring the two questions together:
reviews.loc[(reviews.nationality == "Portugal") & (reviews.age >= 30)]

#Suppose we need any player that is Portuguese or above 30 year olds. we use pipe (|)
reviews.loc[(reviews.nationality == "Portugal") | (reviews.age >= 30)]


# <isin> is lets you select data whose value "is in" a list of values. For example, here's how we can use it to select player only from Italy or France:
reviews.loc[reviews.nationality.isin(['Italy','France'])]

#The second is isnull (and its companion notnull). These methods let you highlight values which are (or are not) empty (NaN). For example, to filter out wines lacking a long shots in the dataset, here's what we would do:
reviews.loc[reviews.long_shots.isnull()]