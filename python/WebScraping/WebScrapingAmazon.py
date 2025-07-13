import requests
import pandas as pd
from bs4 import BeautifulSoup

#this is how we do officially but we have internet issues
# def fetchURLandSaveToFile(url, path):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
#     }
#     if r.status_code != 200:
#         print("Error: ", r.status_code)
#         return
    
#     with open(path, "w", encoding="utf-8") as file: 
#         file.write(r.text)

# url = "https://books.toscrape.com"
# r = requests.get(url)
# fetchURLandSaveToFile(url,"webScapeAmazon.html")
#soup = BeautifulSoup(r.text, "html.parser")

with open("webScapeAmazon.html","r") as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc,"html.parser")

# bookTitle = soup.find(title = "A Light in the Attic")
# print(bookTitle.text) 

data = []

storeAllBooks = soup.select("article.product_pod")  #tis is a list of all books

for book in storeAllBooks:
    title = book.h3.a.text
    price = book.find("p", class_="price_color").text
    stockStatus = book.find("p", class_="instock availability").get_text(strip=True)
    rating_class = book.find("p", class_="star-rating")["class"]    #look in p tag with class star-rating and you will understand these 2 lines of code
    rating = rating_class[1]    #first class is star-rating, this is verified above and 2nc class tells actual rating so we store it

    print("Title: ", title, "\tPrice: ", price, "\tStatus: ", stockStatus, "\tRating: ", rating)

    data.append({
        "Title": title,
        "Price": price,
        "Stock": stockStatus,
        "Rating": rating
    })

df = pd.DataFrame(data) #convert dict to dataframe
df.to_excel("WebScrapedBooks.xlsx", index=False)
print("Saved to File Successfully")