import os
from pydub import AudioSegment


def Mp4ToMp3(songName):
    files = os.listdir()

    for x in files:
        if x.endswith('.mp4'):
            
            os.rename(x, "songs/" + songName + ".mp3") 

#When a song is saved its info in the database, its moved to checked folder in songs
def SongAlreadyRegistered(info):
    info = info
    files = os.listdir('songs/')
    for x in files:
        if x.endswith(".mp3"):
            ##x_clean is x but without spaces
            # x_clean = x.replace(' ', '')
            # print(x_clean)
            # os.rename("songs/" + x,'songs/checked/' + x_clean)
 
            #print(info[0])

            x_clean = str(info[0]) + str(info[1]) + ".mp3"
            x_clean = x_clean.replace(' ', '')
            print("Saved as " + x_clean)
            os.rename("songs/" + x,'songs/checked/' + x_clean)
            return x_clean


def SongAlreadyRegisteredNoInfo():
    files = os.listdir('songs/')
    for x in files:
        if x.endswith(".mp3"):
            #x_clean is x but without spaces
            x_clean = x.replace(' ', '')
            #print(x_clean)
            os.rename("songs/" + x,'songs/checked/' + x_clean)
            return x_clean
