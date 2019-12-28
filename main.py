import downloader
import converter
import extractor


converter.Mp4ToMp3(downloader.Run(0,False))
extractor.GetInfo()
converter.SongAlreadyRegistered()