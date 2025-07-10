import pandas as pd

df = pd.read_csv('pokemon_data.csv')
print(df.sort_values('HP')) #sort pokemons with more HP
print(df.sort_values('Attack', ascending=False))    #sort in descending
