import requests
import pandas as pd
from bs4 import BeautifulSoup

# Step 1: Download the page
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
html_doc = requests.get(url)

# Step 2: Save HTML content to file
with open("netflixStockScraping.html", "w", encoding="utf-8") as file:
    file.write(html_doc.text)  

# Step 3: Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_doc.text, "html.parser") 

# Step 4: Create a dataframe with empty columns of which we need the data
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# Step 5: Find table and it's rows
table = soup.find('tbody').find_all('tr')

#Step 6: Iterate over each row
for row in table:
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

    #Step 7: Append the data we got from website into the dataframe we created
    netflix_data = pd.concat([netflix_data,
        pd.DataFrame({
            "Date":[date],
            "Open":[Open], 
            "High":[high], 
            "Low":[low], 
            "Close":[close], 
            "Adj Close":[adj_close], 
            "Volume":[volume]
            })], 
        ignore_index=True)    

netflix_data.to_excel("netflix_stock_data.xlsx", index=False)
print(netflix_data.head())