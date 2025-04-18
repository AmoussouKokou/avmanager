from media.audio import AudioProcessor
from media.video import VideoProcessor
from media.youtube import YouTubeDownloader

def traiter_fichier(chemin):
    if chemin.endswith((".mp3", ".wav")):
        audio = AudioProcessor(chemin)
        return audio.convertir_audio("wav")
    elif chemin.endswith((".mp4", ".avi")):
        video = VideoProcessor(chemin)
        return video.convertir_video("avi")
    else:
        return None

def telecharger_depuis_youtube(lien, dossier):
    telechargeur = YouTubeDownloader(lien)
    return telechargeur.telecharger(dossier)
