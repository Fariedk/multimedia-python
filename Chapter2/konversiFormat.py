from pydub import AudioSegment

audio = AudioSegment.from_file('naruto.mp3')
audio.export('result.wav', format='wav')