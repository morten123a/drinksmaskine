from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

class Display:
    def __init__(self):
        self.lcd = LCD()
        self.lcd.clear()
        
    def safe_exit(signum, frame):
        exit(1)

    def write_ingredients_on_screen(self, input, id):
        signal(SIGTERM, self.safe_exit)
        signal(SIGHUP, self.safe_exit)

        self.lcd.text(f"{input}", 1)
        self.lcd.text(f"{id}", 2)
        self.lcd.text("Kæft jeg er god", 3)
        pause()

    def get_extra_drink(self, input, amount):
        signal(SIGTERM, self.safe_exit)
        signal(SIGHUP, self.safe_exit)

        self.lcd.text(f"Please put in {amount} cl {input}", 1)

    def destroy(self):
        self.lcd.clear()
