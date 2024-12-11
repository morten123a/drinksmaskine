import gpiod
from time import sleep 

class Pump:
    def __init__(self, pin):
        self.pin = pin
        self.chip = gpiod.Chip('gpiochip4')
        self.pump_line = self.chip.get_line(self.pin)
        self.pump_line.request(consumer="PUMP", type=gpiod.LINE_REQ_DIR_OUT)

    def start(self, centiliters):
        ratio = 5       #Tiden en pumpe tager for at udlevere 1 centiliter
        pouringtime = centiliters * ratio
        self.pump_line.set_value(1)
        sleep(pouringtime)
        self.pump_line.set_value(0)

    def destroy(self):
        self.pump_line.release()
        
