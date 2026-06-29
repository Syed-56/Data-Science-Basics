import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc, "html.parser")
cont = soup.find(class_ = "firstDiv")
cont.name = "span"  #this changes the tag div with calss mentioned to tag span
cont["class"] = "myClass1 myClass2"     #updating class
print(soup.prettify())
