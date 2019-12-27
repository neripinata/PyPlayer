import os
from pydub import AudioSegment

def Mp4ToMp3(songName):
    files = os.listdir()

    for x in files:
        if x.endswith('.mp4'):
            
            os.rename(x, "songs/" + songName + ".mp3") 
