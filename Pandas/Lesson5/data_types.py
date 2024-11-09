import pandas as pd

reviews = pd.read_csv("D:\Lam-Nhat-Tien\CODE\DS & AI\Pandas\Data_set\wine_review\winemag-data-130k-v2.csv",index_col=0)

# viewing column data type:
reviews.points.dtype
reviews.price.dtype

# viewing dtype of whole df:
reviews.dtypes

# change dtype
reviews.points.astype('float64') # here we can see the points under float type while its original type is int

# index also have dtype
reviews.index.dtype