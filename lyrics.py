import speech_recognition as sr
from os import path
from pydub import AudioSegment

src = "songs/checked/Beach House MYTH.mp3"
dst = "songs/checked/Beach House MYTH.wav"

sound = mp4_version = AudioSegment.from_file(src)
sound.export(dst, format="wav")

r = sr.Recognizer()

song = sr.AudioFile("songs/checked/Beach House MYTH.wav")

with song as source:
    audio = r.record(source, duration=30, offset=10)
    
r.recognize_google(audio)