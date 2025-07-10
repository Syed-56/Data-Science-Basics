import requests
import json
import pandas as pd

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)     #retreiving data
pd.DataFrame(results)   #retrieve json data as dataFrame table
#our nutrition columns is still in json format due to nested dictionaries so we have to normalize it
df = pd.json_normalize(results)
print(df)

cherry = df.loc[df["name"]=="Cherry"]
infoCherry = cherry.iloc[0]['family'] + " " + cherry.iloc[0]['genus']
print(infoCherry)

df.drop(columns=["family"],inplace=True)
print(df)