import requests
url = "https://timesofkarachi.pk/category/city/"

r = requests.get(url)
print(r.text)