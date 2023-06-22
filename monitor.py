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


                    #Voltage Ratio(dB)
                    db = 20 * math.log10(rms / reference_power)
                    print(f"Noise Level: {db:.2f} dB")

                    if db > t:
                        stream.stop()
                        print(f"Recording Initiated...")
                        stream.start() 
                        
            except KeyboardInterrupt:
                pass

        # Stop the audio stream
        stream.stop()

if __name__ == "__main__":
    Main.Active()
