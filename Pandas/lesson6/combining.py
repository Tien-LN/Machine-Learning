import pandas as pd

canadian_youtube = pd.read_csv("D:\Lam-Nhat-Tien\CODE\DS & AI\Pandas\Data_set\youtube_trending_video\CAvideos.csv")
british_youtube = pd.read_csv("D:\Lam-Nhat-Tien\CODE\DS & AI\Pandas\Data_set\youtube_trending_video\GBvideos.csv")

canadian_youtube
british_youtube

#  Given a list of elements, concat() function will smush those elements together along an axis.
pd.concat([canadian_youtube,british_youtube])

# The middlemost combiner in terms of complexity is join(). join() lets you combine different DataFrame objects which have an index in common. For example, to pull down videos that happened to be trending on the same day in both Canada and the UK, we could do the following:
left = canadian_youtube.set_index(['title','trending_date'])
right = british_youtube.set_index(['title','trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK') 
