import pandas as pd

df = pd.read_csv('pokemon_data.csv')
print(df.columns)

#reading specefic column
print(df['Name'])
print(df['Speed'][0:5]) #print specific rows of Speed

print(df[['Name', 'HP', 'Attack']]) #print multiple columns