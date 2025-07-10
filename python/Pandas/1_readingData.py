import pandas as pd

df = pd.read_csv('pokemon_data.csv')    #df stores data of csv file in it using pd's function
# print(df)
print(df.head(4))   # head function prints speciefied rows from top 
print(df.tail(3))   #tail function prints specified rows from bottom