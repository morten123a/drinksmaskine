from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

class Display:
    def __init__(self):
        self.lcd.clear()
    
    def safe_exit(signum, frame):
        exit(1)

    def write_ingredients_on_screen(self, input, id):
        self.lcd = LCD()
        signal(SIGTERM, self.safe_exit)
        signal(SIGHUP, self.safe_exit)

        self.lcd.text(input, 1)
        self.lcd.text(id, 2)
        self.lcd.text("Kæft jeg er god", 3)
        pause()


    def destroy(self):
        self.lcd.clear()
