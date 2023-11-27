import http.client

conn = http.client.HTTPSConnection("twitter-api47.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "e24b6a486amsh461e479cbe8e01fp10f331jsnc5ea62aebd0e",
    'X-RapidAPI-Host': "twitter-api47.p.rapidapi.com"
}


id_file = open("ids.txt","r")
id_file = id_file.readlines()
for i in range(10):#range(len(file)):
    current = str(int(id_file[i]))
    conn.request("GET", "/v1/tweet-details?tweetId="+current, headers=headers)
    res = conn.getresponse()
    data = res.read()
    x = (data.decode("utf-8"))
    outputs_file = open("outputs.txt","a",encoding='utf-8')
    outputs_file.write(current+","+x+"\n")
    outputs_file.close()

