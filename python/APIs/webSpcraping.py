from bs4 import BeautifulSoup
import requests

with open("webSpcraping.html", "r") as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())  #create nested structure

title = soup.title.text
print("Title: ", title)

p1 = soup.h3
p1Salary = soup.p
print("Name: ", p1.text, "\tSalary: ", p1Salary.text)

p2 = p1.find_next('h3')
p2Salary = p1Salary.find_next('p')
print("Name: ", p2.text, "\tSalary: ", p2Salary.text, "\n\n")

#but this is inefficient we want to retrieve all players and salaries

names = soup.find_all('h3')
for name in names:
    salary = name.find_next_sibling('p')
    if salary:
        print("Name: ", name.text, "\tSalary: ", salary.text)