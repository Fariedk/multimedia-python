from pydub import AudioSegment

audio = AudioSegment.from_file('naruto.mp3')

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')