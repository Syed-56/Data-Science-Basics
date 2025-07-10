import requests

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"

req = requests.get(url)
if req.status_code==200:
    with open("writingFromAPItoFile.txt", "wb") as f:   #because retrieved content is in bytes
            f.write(req.content)

else:
      print(f"Error: {req.status_code}")