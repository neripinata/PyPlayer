from googlesearch import search
import os
import requests


files = os.listdir("songs/")

substring = "artist"

for x in files:
    if x.endswith('.mp3'):
        query = x
        for j in search(query, tld="co.in", num=10, start=1, stop=4, pause=2): 
            response = requests.get(j)
            print(j)
            print (response.status_code)
            info = response.content
            
            info = str(info)
            count = info.count(substring)
            print(count)

