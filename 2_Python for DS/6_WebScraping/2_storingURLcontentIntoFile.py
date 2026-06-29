import requests

def fetchURLandSaveToFile(url, path):
    r = requests.get(url)
    if r.status_code != 200:
        print("Error: ", r.status_code)
        return
    
    with open(path, "w", encoding="utf-8") as file: #we did encoding parameter so that it can fetch urdu texta aswell
        file.write(r.text)
        print("Content from url written into file ", path)

url = "https://timesofkarachi.pk/category/city/"
fetchURLandSaveToFile(url,"times.html")