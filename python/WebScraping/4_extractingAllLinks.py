import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc,"html.parser")

for link in soup.find_all('a'):
    print(link)     #print all link tags
    print(link.get('href')) #prints actual links
    print(link.get_text())  #gets linke text