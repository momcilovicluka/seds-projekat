import pandas as pd
import random as ra
import numpy as np

# read csv
df = pd.read_csv('/home/luka/Downloads/SEDS/archive/steamShort.csv')

# drop everything except developers
df = df.drop(['appid', 'type', 'name', 'required_age', 'dlc', 'fullgame', 'supported_languages', 'publishers', 'packages', 'platforms', 'categories', 'genres', 'achievements', 'release_date', 'supported_audio', 'coming_soon', 'price', 'review_score', 'total_positive', 'total_negative', 'rating', 'owners', 'average_forever', 'median_forever', 'tags'], axis=1)

# extract only first developer from the list
df['name'] = df['developers'].str.split(',').str[0]

# drop developers column
df = df.drop(['developers'], axis=1)

df['name'] = df['name'].str.replace('[\[\],\']', '', regex=True)

# drop duplicates
df = df.drop_duplicates()

# reset index
df = df.reset_index(drop=True)

# Add a new column with random numbers between 1 and 10
df['countryId'] = np.random.randint(1, 11, size=len(df))

# export to csv index by one
df.to_csv('/home/luka/git/momcilovicluka/seds-projekat/SQLImports/developer.csv', index=True)
