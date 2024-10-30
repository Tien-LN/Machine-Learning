import pandas as pd

student_math = pd.read_csv("D:\Lam-Nhat-Tien\CODE\DS & AI\Pandas\Data_set\student/student-mat.csv",sep=';')
print(student_math.shape)
# this should give us the output: (a,b) which mean our DataFrame has 'a' records split across b columns

#We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:
student_math.head()