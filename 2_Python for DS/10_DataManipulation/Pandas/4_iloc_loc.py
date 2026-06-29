import pandas as pd

df = pd.read_csv('pokemon_data.csv')
print(df.iloc[0])                   # First row (by index)
print(df.iloc[0:3])                 # First 3 rows
print(df.loc[1])                    # Row with label/index 1
print(df.loc[0:2, ['Name', 'HP']])  # Slice rows & columns