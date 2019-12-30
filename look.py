# import urllib.request, urllib.error, urllib.parse
# import scrapy
# import re
# from bs4 import BeautifulSoup

##for www.lyrics.com

# url = 'https://www.lyrics.com/lyric/26337015/Beach+House/Myth'

# def Extraer(url):
#     response = urllib.request.urlopen(url)
#     webContent = response.read().decode()

#     soup = BeautifulSoup(webContent)

#     nameSong = soup.h1.string

#     Artist = soup.h3.subheading

#     for x in soup.find_all('h3'):
#         Artist = x.text
#         Artist = Artist.rstrip(" \xa0Buy This Song\n")
#         break


#     info = [nameSong, Artist]

#     return info

#####################################################################################

# import urllib.request, urllib.error, urllib.parse
# import scrapy
# import re
# from bs4 import BeautifulSoup


# url = 'https://www.letras.com/muse/71970/'


# response = urllib.request.urlopen(url)
# webContent = response.read().decode()

# soup = BeautifulSoup(webContent)

# nameSong = soup.h1.string

# for x in soup.find_all('h1'):
#     nameSong = x.text
    

# for x in soup.find_all('h2'):
#     Artist = x.text
#     break


# info = [nameSong, Artist]

# print(info)

#########################################################################################

import urllib.request, urllib.error, urllib.parse
import scrapy
import re
from bs4 import BeautifulSoup


def Extraer_from_letras(url):
    #to look in letras.com
    letra = ""

    response = urllib.request.urlopen(url)
    webContent = response.read().decode()

    soup = BeautifulSoup(webContent)

    nameSong = soup.h1.string

    for x in soup.find_all('h1'):
        nameSong = x.text
            

    for x in soup.find_all('h2'):
        Artist = x.text
        break

    for x in soup.find_all('p'):
        letra += x.text

    letra = letra.replace(" Música comienza con letras © 2003 - 2019, 2.7 millones de canciones  Hecho con amor en Belo Horizonte - Brasil Asociados:Quiero recibir notificaciones de artistas destacados y noticias.", "")

    Artist = Artist.strip()
    info = [nameSong, Artist, letra]

    return info

    

def Extraer_from_lyrics(url):
    #to look in lyrics.com
    response = urllib.request.urlopen(url)
    webContent = response.read().decode()

    soup = BeautifulSoup(webContent)

    nameSong = soup.h1.string

    Artist = soup.h3.subheading

    for x in soup.find_all('h3'):
        Artist = x.text
        Artist = Artist.rstrip(" \xa0Buy This Song\n")
        break


    info = [nameSong, Artist]

    return info

    
