#Main Function
from modules import *
from cloud import *
from settings import *

class Main():
    def Active():
        # Calculate the reference power level (for maximum amplitude of 1)
        reference_power = 1.0

        # Initialize the audio stream
        stream = sd.InputStream(samplerate=sr, channels=ch, blocksize=bs)

        # Start the audio stream
        with stream:
            print("Noise Level Meter - Press Ctrl+C to stop.")
            print("Listening...")

            try:
                while True:
                    data = stream.read(bs)[0]
                    rms = np.sqrt(np.mean(np.square(data)))

                    #Voltage Ratio(dB)
                    db = 20 * math.log10(rms / reference_power)

                    if db > t:
                        stream.stop()

                        name = 'Entry' + str(Logging.Last()) + '.wav'
                        key = folder_dir + name
                        file_data = Audio.Record(name)

                        Cloud.Upload(file_data, BUCKET, key)
                        print(f"Audio uploaded as '{name}'.")
                        stream.start() 
                        
            except KeyboardInterrupt:
                pass

        # Stop the audio stream
        stream.stop()

if __name__ == "__main__":

    i = Button.check()
    if i:
        print('Skip main function...')
        Main.Active()

    else:
        pass
