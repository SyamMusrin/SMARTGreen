#Audio Function
import sounddevice as sd
from io import BytesIO
from scipy.io import wavfile

class Audio:
    @staticmethod
    def Record(d, sr, name, bd):

        # Record audio
        print("Recording audio...")
        recording = sd.rec(
            int(d * sr), 
            samplerate=sr, 
            channels = 1, 
            dtype= 'int' + str(bd),
            blocking = True)

        # Save audio to a .wav file with specified bit depth
        file_data = BytesIO()
        wavfile.write(file_data, sr, recording)

        return file_data
