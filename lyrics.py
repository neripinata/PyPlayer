import speech_recognition as sr
from os import path
from pydub import AudioSegment
import librosa
import math


def GetLyrics(song):
    song = song
    r = sr.Recognizer()


    source = "output/{}/vocals.wav".format(song)
    source_to_doc = "output/{}/".format(song)

    f= open("output/{}/{}.txt".format(song, song),"w+")

    song = sr.AudioFile(source)

    duration = librosa.get_duration(filename=source)
    duration = math.floor(duration)
    tries = int(duration)
    print(tries)

    i = 0

    while i < tries:
        try:
            with song as source:
                audio = r.record(source, duration=5, offset=i)
                f.write(str(i) + str(r.recognize_google(audio)) + "\n")
                print(r.recognize_google(audio))
        except:
            print("Audio is not recognized")
        i += 5

    f.close()

# try:
#     with song as source:
#         audio = r.record(source, duration=5, offset=10)
#         print(r.recognize_google(audio))
# except:
#     print("tried 1 failed")


# try:
#     with song as source:
#         audio = r.record(source)
#         r.recognize_google(audio)
# except:
#     print("tried 4 failed")



#r.recognize_google(audio)