import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import subprocess
import os

root = tk.Tk()
root.title("MP3 Player")
# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)

        # Membuat file sementara dengan delete=False
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
            temp_file_path = temp_audio_file.name
            audio.export(temp_file_path, format="mp3")
            
      # Memainkan audio dengan ffplay
        subprocess.call(['ffplay', '-nodisp', '-autoexit', temp_file_path])

        # Menghapus file sementara setelah pemutaran selesai
        os.remove(temp_file_path)


# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

root.mainloop()