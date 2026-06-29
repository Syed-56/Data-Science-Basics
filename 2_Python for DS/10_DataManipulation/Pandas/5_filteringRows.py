import pandas as pd

df = pd.read_csv('pokemon_data.csv')
print(df[df['HP']>50])
print(df[(df['Generation'] == 6) & (df['Legendary']==True)])