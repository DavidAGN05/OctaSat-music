import RPi.GPIO as GPIO
from time import sleep

class Buzzer:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setwarnings(False)  # Disable GPIO warnings
        GPIO.setmode(GPIO.BCM)  # Set GPIO mode to BCM
        GPIO.setup(self.pin, GPIO.OUT)  # Set pin as output
        self.pwm = GPIO.PWM(self.pin, 1)  # Set PWM on the pin, start with 1Hz frequency

    def play_tone(self, frequency, duration):
        """Plays a tone with the specified frequency and duration."""
        self.pwm.start(50)  # Start PWM with 50% duty cycle
        self.pwm.ChangeFrequency(frequency)  # Change frequency to play the note
        sleep(duration)  # Play for the given duration
        self.pwm.stop()  # Stop PWM after the note is played

    def play_song(self, notes):
        """Plays a sequence of notes. Each note is a tuple (frequency, duration)."""
        for frequency, duration in notes:
            if frequency == 0:  # Rest
                sleep(duration)
            else:
                self.play_tone(frequency, duration)

    def destroy(self):
        """Stops the buzzer and cleans up GPIO."""
        print("[!] Buzzer -- cleaning up GPIO")
        GPIO.cleanup(self.pin)  # Cleanup the specific GPIO pin used by the buzzer

# Define the melody and rhythm for "Hot Cross Buns"
# Notes are in Hz, duration is in seconds
hot_cross_buns = [
    (392, 0.5), (349, 0.5), (330, 1.0),  # "Hot Cross Buns"
    (392, 0.5), (349, 0.5), (330, 1.0),  # "Hot Cross Buns"
    (330, 0.25), (330, 0.25), (330, 0.25), (330, 0.25),  # "One a penny, two a penny"
    (349, 0.5), (349, 0.5),  # "Hot"
    (392, 0.5), (349, 0.5), (330, 1.0)   # "Cross Buns"
]

if __name__ == "__main__":
    buzzer_pin = 18  # Change this to your GPIO pin
    buzzer = Buzzer(buzzer_pin)

    try:
        print("[+] Playing 'Hot Cross Buns'...")
        buzzer.play_song(hot_cross_buns)
    except KeyboardInterrupt:
        print("[!] Interrupted by user")
    finally:
        buzzer.destroy()