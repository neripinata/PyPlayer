from googlesearch import search
import os
import requests
import look
import ddg3


files = os.listdir("songs/")

substring = "artist"

for x in files:
    if x.endswith('.mp3'):
        #x = str(x)
        query = x.rstrip(".mp3")
        print(query)
        try:
            for j in search(query, tld="co.in", num=10, start=1, stop=15, pause=2):
                if "www.letras.com" in j:
                    try:
                        info = look.Extraer_from_letras(j)
                        print(info)

                    except:
                        print("Error connection")
                elif "www.lyrics.com" in j:
                    try:
                        info = look.Extraer_from_lyrics(j)
                        print(info)

                    except:
                        print("Error connection")
        except:
            i = 0
            while i < 20:
                print(query)
                link = ddg3.query(query)
                print(link.related[i].url)
                try:
                    if "www.letras.com" in link.related[i].url:
                        try:
                            info = look.Extraer_from_letras(link.related[i].url)
                            print(info)
                        except:
                            print ("Error connection")
                except:
                    print("nop")
                i += 1




                    

#print(info)