from googlesearch import search
import os
import requests


files = os.listdir("songs/")

substring = "artist"

for x in files:
    if x.endswith('.mp3'):
        #x = str(x)
        query = x.rstrip(".mp3")
        print(query)
        for j in search(query, tld="co.in", num=10, start=1, stop=5, pause=2):
            if "genius.com" in j:
                try:
                    response = requests.get(j)
                    print(j)
                    print (response.status_code)
                    info = response.content
                    
                    info = str(info)
                    count = info.count(substring)
                    print(info)
                    

                except:
                    print("Error connection")

