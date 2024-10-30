import pandas as pd

reviews = pd.read_csv("D:\Lam-Nhat-Tien\CODE\DS & AI\Pandas\Data_set\wine_review\winemag-data-130k-v2.csv",index_col=0)
reviews

# the describe() method generates a high-level summary of the attributes of the given column7
reviews.points.describe()

# It is type-aware, meaning that its output changes based on the data type of the input
# This is output for string data
reviews.designation.describe()

# mean() function (giá trị trung bình)
reviews.points.mean()

# to see a list of unique values we can use unique() func
reviews.taster_name.unique()

# to see a list of unique values and their occurence, use value_counts()
reviews.province.value_counts()