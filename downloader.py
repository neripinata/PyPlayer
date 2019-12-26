from pytube import YouTube
#import libraries for search song
import urllib.request
import urllib.parse
import re

i = 0
alreadyDownladed = False

#Look for link of the song
def SearchSong(songName,i):
    query_string = urllib.parse.urlencode({"search_query" : songName})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    link = "http://www.youtube.com/watch?v=" + search_results[i]
    return link


#Download video from link given by SearchSong
def Download(link):
    try:
        YouTube(link).streams.first().download()
        alreadyDownladed = True
        return alreadyDownladed
    except:
        print("Song isn't available to download")


# songName = input("Name of the song")
# while alreadyDownladed != True:
#     link = SearchSong(songName)
#     alreadyDownladed = Download(link)
#     i += 1


def Run(i,alreadyDownladed):
    songName = input("Name of the song: ")
    while alreadyDownladed != True:
        link = SearchSong(songName, i)
        alreadyDownladed = Download(link)
        i += 1
    return songName

#Run(i,alreadyDownladed)