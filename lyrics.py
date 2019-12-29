import speech_recognition as sr
from os import path
from pydub import AudioSegment

src = "songs/checked/Beach House MYTH.mp3"
dst = "songs/checked/Beach House MYTH.wav"

sound = mp4_version = AudioSegment.from_file(src)
sound.export(dst, format="wav")

r = sr.Recognizer()

song = sr.AudioFile("output/test4/vocals.wav")

try:
    with song as source:
        audio = r.record(source, duration=20, offset=60)
        r.recognize_google(audio)
except:
    print("tried 1 failed")


try:
    with song as source:
        audio = r.record(source, duration=20, offset=80)
        r.recognize_google(audio)
except:
    print("tried 2 failed")


try:
    with song as source:
        audio = r.record(source, duration=20, offset=100)
        r.recognize_google(audio)
except:
    print("tried 3 failed")



#r.recognize_google(audio)