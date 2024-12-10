import gpiod
from time import sleep 

class Pump:
    def __init__(self, pin):
        self.pin = pin
        self.chip = gpiod.Chip('gpiochip4')
        self.led_line = self.chip.get_line(self.pin)
        self.led_line.request(consumer="PUMP1", type=gpiod.LINE_REQ_DIR_OUT)

    def start(self, time_in_seconds: int):
        self.led_line.set_value(1)
        sleep(time_in_seconds)
        self.led_line.set_value(0)

    def destroy(self):
        self.led_line.release()
        
