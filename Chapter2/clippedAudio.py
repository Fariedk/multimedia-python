from pydub import AudioSegment

audio = AudioSegment.from_file('naruto.mp3')
clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')