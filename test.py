import http.client
import time

conn = http.client.HTTPSConnection("twitter-api47.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "421607a060mshba46c4f4cabfe91p1cc11ejsn0ab16aeab3d4",
    'X-RapidAPI-Host': "twitter-api47.p.rapidapi.com"
}

id_file = open("ids.txt","r")
id_file = id_file.readlines()
for i in range(7):#range(len(file)):
    current = str(int(id_file[i]))
    conn.request("GET", "/v1/tweet-details?tweetId="+current, headers=headers)
    res = conn.getresponse()
    data = res.read()
    x = (data.decode("utf-8"))
    outputs_file = open("outputs.txt","a",encoding='utf-8')
    outputs_file.write(current+","+x+"\n")
    outputs_file.close()
    time.sleep(0.5)
