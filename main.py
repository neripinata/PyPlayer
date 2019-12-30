import downloader
import converter
import extractor
import separador
import lyrics


converter.Mp4ToMp3(downloader.Run(0,False))
info = extractor.GetInfo()
#real_lyrics = info[2]
try:
    detected_lyrics = lyrics.GetLyrics(separador.ExtractVoice(converter.SongAlreadyRegistered(info)))
except:
    detected_lyrics = lyrics.GetLyrics(separador.ExtractVoice(converter.SongAlreadyRegisteredNoInfo()))

