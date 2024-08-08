from pydub import AudioSegment
from clippedAudio import clipped_audio

audio = AudioSegment.from_file('naruto.mp3')

combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')