import downloader
import converter
import extractor
import separador
import lyrics


converter.Mp4ToMp3(downloader.Run(0,False))

#Extrae la informacion de la cancion, si encuentra resultados,
#cambia el nombre del archivo a NombreArtista.mp3, si no encuentra resultados lo que
#hara es renombrar el archivo a como el usuario haya puesto la busqueda pero eliminando los
#espacios, despues extaera la voz y el resto de instrumentos
try:
    lyrics.GetLyrics(separador.ExtractVoice(converter.SongAlreadyRegistered(extractor.GetInfo())))
except:
    lyrics.GetLyrics(separador.ExtractVoice(converter.SongAlreadyRegisteredNoInfo()))
    
    
