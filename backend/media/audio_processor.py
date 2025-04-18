from pydub import AudioSegment
from moviepy.editor import concatenate_audioclips
from .base import MediaHandler

class AudioProcessor(MediaHandler):
    def extraire_audio(self, sortie_audio):
        audio = AudioSegment.from_file(self.chemin_media)
        audio.export(sortie_audio, format="mp3")

    def convertir_audio(self, format_sortie):
        audio = AudioSegment.from_file(self.chemin_media)
        sortie = self.chemin_media.rsplit(".", 1)[0] + "." + format_sortie
        audio.export(sortie, format=format_sortie)
        return sortie

    def decouper_audio(self, debut, fin, sortie_audio):
        audio = AudioSegment.from_file(self.chemin_media)
        extrait = audio[debut * 1000:fin * 1000]
        extrait.export(sortie_audio, format="mp3")

    def fusionner_audios(self, liste_audios, sortie_audio):
        clips = [AudioSegment.from_file(audio) for audio in liste_audios]
        audio_fusionne = sum(clips)
        audio_fusionne.export(sortie_audio, format="mp3")
