import os

#spleeter separate -i spleeter/audio_example.mp3 -p spleeter:2stems -o output

file = "RideIt.mp3"

file = "songs/checked/{}".format(file)

#command = 'cmd /c' + "spleeter separate -i " + file + " -p spleeter:2stems -o output"

os.system('cmd /c "conda activate PyLab & spleeter separate -i {} -p spleeter:2stems -o output"'.format(file))
os.system('cmd /c "conda deactivate"')


#os.system('cmd /c "spleeter separate -i songs/checked/test4.mp3 -p spleeter:2stems -o output"')