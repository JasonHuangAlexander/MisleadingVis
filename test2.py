import requests
import os

ok = open("outputs.txt","r",encoding='utf-8')
ok = ok.readlines()
count = 0
for line in ok:
    count = count+1
    try:
        string = line
        string = string.split("\"media_url_https\":\"")
        string = string[1].split("\",\"type\":")
        string = string[0]
        print(string)
        img_data = requests.get(string).content
        path = r"C:\Users\local1\sarvghad visualizations\Twitter API stuff\\"
        string = line
        string = string.split(",")[0]
        current = f"{string}.jpg"
        with open(os.path.join(path,current),"wb") as handler:
            handler.write(img_data)
        print("OK!")
    except:
        continue

