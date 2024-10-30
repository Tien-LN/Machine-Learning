import pandas as pd

reviews = pd.read_csv("D:\Lam-Nhat-Tien\CODE\DS & AI\Pandas\Data_set\student/student-por.csv",sep=';')
reviews

'''In Python, we can access the property of an object by accessing it as an attribute
   by using  < object_name.property_title > '''
reviews.school
# or
reviews["school"]

###### INDEXING ###### 
''' Index-based selection (iloc) '''
reviews.iloc[0]

#To get a column with iloc, we can do the following:
reviews.iloc[:,0]

#to select the first column from just the first, second, and third row, we would do:
reviews.iloc[:3,0]

#Or, to select just the second and third entries, we would do:
reviews.iloc[1:3,0]

#It's also possible to pass a list:
reviews.iloc[[0,3,644],0]

''' Label-based selection (loc) '''
#to get the first entry in reviews, we would now do the following:
reviews.loc[0,'school']
#---
reviews.loc[:,['sex','age','address']]

###### Manipulating the index #####
reviews.set_index("Fjob")
#This is useful if you can come up with an index for the dataset which is better than the current one.