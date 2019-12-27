from googlesearch import search
import os
import requests
import look


files = os.listdir("songs/")

substring = "artist"

for x in files:
    if x.endswith('.mp3'):
        #x = str(x)
        query = x.rstrip(".mp3")
        print(query)
        for j in search(query, tld="co.in", num=10, start=1, stop=30, pause=2):
            if "www.letras.com" in j:
                try:
                    # response = requests.get(j)
                    # print(j)
                    # print (response.status_code)
                    # info = response.content
                    
                    # info = str(info)
                    # count = info.count(substring)
                    #print(info)
                    
                    info = look.Extraer(j)
                    print(info)

                except:
                    print("Error connection")

#print(info)