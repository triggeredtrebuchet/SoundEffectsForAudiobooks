import tkinter as tk
from tkinter import filedialog
import librosa
import soundfile as sf
from sound_effects import transcript
import pyaudio
import numpy as np


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.original_audiobook_layer = None
        self.enhenced_audiobook_layer = None
        self.sample_rate = None
        self.title("Sound Effects for audiobooks")
        self.geometry("430x270")

        self.aoudiobuttons_frame = tk.Frame(self)

        self.load_button = tk.Button(self.aoudiobuttons_frame, text="Load", command=self.choose_file)
        self.load_button.pack(side="top", padx=20, pady=20)

        self.play_button = tk.Button(self.aoudiobuttons_frame, text="Play", command=self.play_file, state="disabled")
        self.play_button.pack(side="top", padx=20, pady=20)

        self.save_button = tk.Button(self.aoudiobuttons_frame, text="Save", command=self.save_file, state="disabled")
        self.save_button.pack(side="top", padx=20, pady=20)

        self.add_sfx_button = tk.Button(self.aoudiobuttons_frame, text="play with sound effects", command=self.play_with_sfx_file,
                                   state="disabled")
        self.add_sfx_button.pack(side="top", padx=20, pady=20)

        self.aoudiobuttons_frame.pack(side="left", fill="both", expand=True)

    def choose_file(self):
        filepath: str = filedialog.askopenfilename(filetypes=[("Pliki MP3 i WAV", "*.mp3;*.wav")])
        if filepath:
            self.filepath = filepath
            self.play_button.config(state="normal")
            self.add_sfx_button.config(state="normal")
            self.save_button.config(state="normal")
            self.original_audiobook_layer, self.enhenced_audiobook_layer, self.sample_rate = transcript.add_sound_effects(filepath)
        else:
            pass

    def save_file(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".wav")
        sf.write(save_path, self.enhenced_audiobook_layer, self.sample_rate, "PCM_24")

    def play_file(self):
        audioPlayer = pyaudio.PyAudio()
        # Utworzenie strumienia audio
        stream = audioPlayer.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=self.sample_rate,
                        output=True)

        stream.write(self.original_audiobook_layer.astype(np.float32).tobytes())

        stream.stop_stream()
        stream.close()
        audioPlayer.terminate()

    def play_with_sfx_file(self):
        audioPlayer = pyaudio.PyAudio()
        stream = audioPlayer.open(format=pyaudio.paFloat32,
                                       channels=1,
                                       rate=self.sample_rate,
                                       output=True)

        stream.write(self.enhenced_audiobook_layer.astype(np.float32).tobytes())

        stream.stop_stream()
        stream.close()
        audioPlayer.terminate()



root = Root()
root.mainloop()
