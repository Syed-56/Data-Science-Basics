import requests
from bs4 import BeautifulSoup

with open("sample.html","r", encoding="utf-8") as file:
    html_doc = file.read()  #storing html content in a string

soap = BeautifulSoup(html_doc,"html.parser")    #making soap object from html string
#print(soap.prettify())  formats object into readable html

print(soap.title, type(soap.title))   #soap.title prints title tag of html and type tells the class of it 
print(soap.title.name)  #this only tells the tag of title (which is title)
print(soap.title.text)  #this tells the text inside title

print(soap.div) #returns first div
print(soap.div.p)   #returns p tag inside 1st div
print(soap.find_all('div')) #returns all divs