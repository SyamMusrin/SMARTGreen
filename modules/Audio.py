#Recording Function
import sounddevice as sd
from scipy.io import wavfile
import os
from time import sleep

class Audio():
    def Record(duration, sample_rate, num):
        # Set the sample rate and duration
        fs = sample_rate  # Sample rate (Hz)
        duration_s = duration  # Duration of recording (seconds)

        # Record audio
        print("Recording audio...")
        recording = sd.rec(int(duration_s * fs), samplerate=fs, channels=1)
        sd.wait()  # Wait until recording is finished

        #Extract data
        folder_name = os.getcwd() + "/recordings/"
        file_name = "Entry" + num + ".wav"
        file_dir = folder_name + file_name

        # Save audio to a .wav file
        wavfile.write(file_dir, fs, recording)

        print(f"Audio saved as '{file_name}'.")
