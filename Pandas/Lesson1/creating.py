from IPython.display import display
import pandas as pd     # used for data manipulation and analysis

# pd.DataFrame() is a constructor, it looks like a table

df1 = pd.DataFrame({'yes': [50, 100], 'no': [30, 70]})

df2 = pd.DataFrame({'Andrew': ["male", "18ys"], 'Lisa': ["female", "17ys"]})

''' 
The list of row labels used in a DataFrame is known as an Index.
We can assign values to it by using an index parameter in our constructor: '''

df3 = pd.DataFrame({'Andrew':["male","18"],
                    'Lisa':["female","17"]},
                    index=["gender","age"])

df4=pd.DataFrame({'Ty':["eldest son",1999],
                  'Tien':["middle son",2005],
                  'Huy':["youngest son",2012]},
                  index=["role","born year"])

#display
display(df1)
display(df2)
display(df3)
display(df4)

# A series is a sequence of data values. If DataFrame is a table, a series is a list

s1 = pd.Series([1,2,3,4,5])
display(s1)

'''
A series is, in essence (về cơ bản), a single column of a DataFrame.
So we can assign row labels just like DF using index.
a series doesn't have column name, it only have one overall name
'''

s2 = pd.Series([30,50,80], 
               index=(["2020 sales","2021 sales","2022 sales"]),
               name="product A")
display(s2)

# use DFname.to_csv("name we want") to save the data frame to disk as a csv file 

