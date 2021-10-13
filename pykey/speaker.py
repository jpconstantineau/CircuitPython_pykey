import time
import pwmio

class KB_Speaker:

    def __init__(self, speaker_pin):

        self.speaker_pin = speaker_pin
        self.buzzer = pwmio.PWMOut(speaker_pin, variable_frequency=True)
        self.buzzer.frequency = 440

    def play_startup_tune(self):
        OFF = 0  # pylint: disable=invalid-name
        ON = 2**15  # pylint: disable=invalid-name
        self.buzzer.duty_cycle = ON
        self.buzzer.frequency = 440
        time.sleep(0.05)
        self.buzzer.frequency = 880
        time.sleep(0.05)
        self.buzzer.frequency = 1660
        time.sleep(0.05)
        self.buzzer.duty_cycle = OFF

    def play_shutdown_tune(self):
        OFF = 0  # pylint: disable=invalid-name
        ON = 2**15  # pylint: disable=invalid-name
        self.buzzer.duty_cycle = ON
        self.buzzer.frequency = 1660
        time.sleep(0.05)
        self.buzzer.frequency = 880
        time.sleep(0.1)
        self.buzzer.frequency = 440
        time.sleep(0.15)
        self.buzzer.duty_cycle = OFF

    def start_tone(self, frequency):
        OFF = 0  # pylint: disable=invalid-name
        ON = 2**15  # pylint: disable=invalid-name
        self.buzzer.frequency = frequency
        self.buzzer.duty_cycle = ON

    def stop_tone(self):
        OFF = 0  # pylint: disable=invalid-name
        ON = 2**15  # pylint: disable=invalid-name
        self.buzzer.duty_cycle = OFF
    

