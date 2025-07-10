import pandas as pd

dfExcel = pd.read_excel('pokemon_data.xlsx')
print(dfExcel)

dfTxt = pd.read_csv('pokemon_data.txt', delimiter = '\t')   #if we dont use delimeter than tab will be apperaing to seperate column but using delimeter tell to seperate output when we see tab
print(dfTxt)