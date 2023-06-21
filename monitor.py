#Main Function
from modules import *
from cloud import *
from settings import *

class Main():
    def Active():
        # Calculate the reference power level (for maximum amplitude of 1)
        reference_power = 1.0

        # Initialize the audio stream
        stream = sd.InputStream(samplerate=sr, channels=1, blocksize=bs)

        # Start the audio stream
        with stream:
            print("Noise Level Meter - Press Ctrl+C to stop.")
            print("Listening...")

            try:
                while True:
                    data = stream.read(bs)[0]
                    rms = np.sqrt(np.mean(np.square(data)))
                    db = 20 * math.log10(rms / reference_power)
                    print(f"Noise Level: {db:.2f} dB")

                    if db > t:
                        now = datetime.now()
                        date = now.strftime("%d/%m/%Y")
                        time = now.strftime("%H:%M:%S")

                        Logging.New_Entry(date, time)
                        name = 'Entry' + str(Logging.Last()) + '.wav'
                        file_data = Audio.Record(d = d, sr = sr, name = name, bd = bd)

                        Cloud.Upload(file_data, BUCKET, name)
                        print(f"Audio uploaded as '{name}'.")
                        
            except KeyboardInterrupt:
                pass

        # Stop the audio stream
        stream.stop()

if __name__ == "__main__":
    Main.Active()