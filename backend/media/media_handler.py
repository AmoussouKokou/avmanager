import os

class MediaHandler:
    def __init__(self, chemin_media):
        self.chemin_media = chemin_media
        self.type_media = self.detection_type_media()

    def detection_type_media(self):
        extension = os.path.splitext(self.chemin_media)[1].lower()
        if extension in [".mp3", ".wav", ".aac", ".flac"]:
            return "audio"
        elif extension in [".mp4", ".avi", ".mov", ".mkv"]:
            return "video"
        else:
            return "inconnu"
