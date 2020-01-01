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

    lang = "en-US"

    while i < tries:
        with song as source:
            r.adjust_for_ambient_noise(source)            
            try:
                audio = r.record(source, duration=1, offset=i)
                f.write(str(i) + str(r.recognize_google(audio, language=lang)) + "\n")
                #print(r.recognize_google(audio, language=lang))
                i += 1
            except:
                try:
                    print("Try 1 - Unrecognize audio at " + str(i))
                    audio = r.record(source, duration=2, offset=i)
                    f.write(str(i) + str(r.recognize_google(audio, language=lang)) + "\n")
                    #print(r.recognize_google(audio, language=lang))
                    i += 2
                except:
                    try:
                        print("Try 2 - Unrecognize audio at " + str(i))
                        audio = r.record(source, duration=3, offset=i)
                        f.write(str(i) + str(r.recognize_google(audio, language=lang)) + "\n")
                        #print(r.recognize_google(audio, language=lang))
                        i += 3
                    except:
                        try:
                            print("Try 3 - Unrecognize audio at " + str(i))
                            audio = r.record(source, duration=4, offset=i)
                            f.write(str(i) + str(r.recognize_google(audio, language=lang)) + "\n")
                            #print(r.recognize_google(audio, language=lang))
                            i += 4
                        except:
                            print("Try 4 - Unrecognize audio at " + str(i))
                            i += 4

            print(i)


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