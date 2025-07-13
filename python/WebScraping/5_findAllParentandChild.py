import requests
from bs4 import BeautifulSoup

with open("sample.html","r", encoding="utf-8") as file:
    html_doc = file.read()  

soap = BeautifulSoup(html_doc,"html.parser")
for child in soap.find('div').children:
    print(child)

for parent in soap.find('div').parent:
    print(parent)