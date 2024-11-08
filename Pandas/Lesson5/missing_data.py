import pandas as pd

reviews = pd.read_csv("D:\Lam-Nhat-Tien\CODE\DS & AI\Pandas\Data_set\wine_review\winemag-data-130k-v2.csv",index_col=0)

# Entries missing values are given the value NaN ( not a number ), for technical reason these NaN have float64 dtype
# to select NaN entries we use pd.isnull() ( we also have pd.notnull() as its companion )
reviews[pd.isnull(reviews.country)]

# replace missing value using fillna()
# for example: we can replace each NaN with 'UnKnown'
reviews.region_2.fillna("UnKnown")

''' Alternatively, we may have a non-null value that we would like to replace. 
 For example, suppose that since this dataset was published, reviewer Kerin O'Keefe 
 has changed her Twitter handle from @kerinokeefe to @kerino. One way to reflect this 
 in the dataset is using the replace() method:'''

reviews.taster_twitter_handle.replace("@kerinokeefe","@kerino")

'''The replace() method is worth mentioning here because it's handy 
   for replacing missing data which is given some kind of sentinel value
   in the dataset: things like "Unknown", "Undisclosed", "Invalid", and so on.'''