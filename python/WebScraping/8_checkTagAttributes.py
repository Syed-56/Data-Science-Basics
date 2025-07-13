import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc,"html.parser")

cont = soup.find(class_ = "firstDiv")
print(cont.has_attr("class"), cont.has_attr("id"))

def hasClassButNotID(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

results = soup.find_all(hasClassButNotID)
for tag in results:
    print(results)  #this will print all tags which have class but not Id