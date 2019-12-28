import os
from pydub import AudioSegment

def Mp4ToMp3(songName):
    files = os.listdir()

    for x in files:
        if x.endswith('.mp4'):
            
            os.rename(x, "songs/" + songName + ".mp3") 

#When a song is saved its info in the database, its moved to checked folder in songs
def SongAlreadyRegistered():
    files = os.listdir('songs/')
    for x in files:
        if x.endswith(".mp3"):
            os.rename("songs/" + x,'songs/checked/' + x)