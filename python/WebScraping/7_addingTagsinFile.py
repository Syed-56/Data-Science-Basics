import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc,"html.parser")

ulTag = soup.new_tag("ul")

liTag = soup.new_tag("li")
liTag.string = "Home"
ulTag.append(liTag) #liTag is now inside ulTag

liTag = soup.new_tag("li")
liTag.string = "About"
ulTag.append("About")

soup.html.body.insert(0,ulTag)  #in body tag of html, at 0th index the ulTag is now inserted

with open("sampleModified.html", "w") as file:
    file.write(str(soup))