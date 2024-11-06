import pandas as pd

reviews = pd.read_csv("D:\Lam-Nhat-Tien\CODE\DS & AI\Pandas\Data_set\wine_review\winemag-data-130k-v2.csv",index_col=0)

# GROUP --------------------------------------------------------------
# Groupwise analysis - Phan tich theo nhom
reviews.groupby('points').points.count()

'''groupby() created a group of reviews which allotted the same point values to the given wines. Then, for each of these groups, we grabbed the points() column and counted how many times it appeared.'''

# we can use any of the summary functions we've used before with this data. For example, to get the cheapest wine in each point category, we do:
reviews.groupby('points').price.min()
# or in each country:
reviews.groupby('country').price.min()

'''We can thing of each group we generate as being a slice of our DF containing 
only data with values that match.  This DataFrame is accessible to us directly using the apply() method, and we can then manipulate the data in any way we see fit. 
For example, here's one way of selecting the name of the first wine reviewed from each winery in the dataset:''' # winery : nha may ruou.
reviews.groupby('winery').apply(lambda df : df.title.iloc[0])

# here how we would pick out the best wine by country and province:
reviews.groupby(['country','province']).apply(lambda df : df.loc[df.points.idxmax()])

# agg() let we run a bunch of different functions on our DF simultaneously.
# ex: we can generate a simple statical summary of the dataset as follow:
reviews.groupby('country').price.agg([len,min,max])

# MULTI INDEXES -------------------------------------------------------
contries_reviewed = reviews.groupby(['country','province']).description.agg([len])
contries_reviewed

mi = contries_reviewed.index
type(mi)

# in general the multi-index method you will use most often is the one for converting back to a regular index, the reset_index() method:
contries_reviewed = contries_reviewed.reset_index()
contries_reviewed

# SORTING ------------------------------------------------------------
# To get data in the order want it in we can sort it ourselves. The sort_values() method is handy (tien loi) for this.
contries_reviewed.sort_values(by='len')
# descending sort:
contries_reviewed.sort_values(by='len', ascending=False)
# To sort by index values, use the companion method sort_index(). This method has the same arguments and default order:
contries_reviewed.sort_index()
# we can sort more than one column at a time
contries_reviewed.sort_values(by=(['country','len']))
