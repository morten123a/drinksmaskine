from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from time import sleep

class Display:
    def __init__(self):
        self.lcd = LCD()
        self.lcd.clear()
        
    def safe_exit(signum, frame):
        exit(1)

    def write_ingredients_on_screen(self, input, id):
        self.lcd.clear()
        signal(SIGTERM, self.safe_exit)
        signal(SIGHUP, self.safe_exit)

        self.lcd.text(f"Drinknavn: {input}", 1)
        self.lcd.text(f"Drinknummer: {id}", 2)


    def get_extra_drink(self, input, amount):
        self.lcd.clear()
        signal(SIGTERM, self.safe_exit)
        signal(SIGHUP, self.safe_exit)

        self.lcd.text(f"Please put in {amount} cl {input}", 1)
        sleep(3)

    def destroy(self):
        self.lcd.clear()
