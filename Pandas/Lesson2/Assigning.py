import pandas as pd

reviews = pd.read_csv("D:\Lam-Nhat-Tien\CODE\DS & AI\Pandas\Data_set/fifa_players.csv",index_col=0)

# We can assign either a constant value:
reviews['full_name'] = 'Ronaldo'
reviews['full_name']

# Or with an iterable of values:
reviews['index_backwards'] = range(len(reviews), 0, -1)
reviews['index_backwards']
