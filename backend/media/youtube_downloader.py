from pytube import YouTube
import os

class YouTubeDownloader:
    def __init__(self, lien_youtube):
        self.lien_youtube = lien_youtube
        self.youtube = YouTube(lien_youtube)

    def telecharger(self, chemin_sortie):
        stream = self.youtube.streams.get_highest_resolution()
        fichier = stream.download(output_path=chemin_sortie)
        return fichier