import RPi.GPIO as GPIO

class Button:
    def check():
        BUTTON = 17

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUTTON, GPIO.IN)
        state = GPIO.input(BUTTON)

        return state
