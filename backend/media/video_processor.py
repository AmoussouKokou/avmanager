from moviepy.editor import VideoFileClip, concatenate_videoclips
from .base import MediaHandler

class VideoProcessor(MediaHandler):
    def convertir_video(self, format_sortie):
        clip = VideoFileClip(self.chemin_media)
        sortie = self.chemin_media.rsplit(".", 1)[0] + "." + format_sortie
        clip.write_videofile(sortie)
        return sortie

    def decouper_video(self, debut, fin, sortie_video):
        clip = VideoFileClip(self.chemin_media).subclip(debut, fin)
        clip.write_videofile(sortie_video)

    def fusionner_videos(self, liste_videos, sortie_video):
        clips = [VideoFileClip(video) for video in liste_videos]
        video_fusionnee = concatenate_videoclips(clips)
        video_fusionnee.write_videofile(sortie_video)
