from database import Database
from display import Display
from pump import Pump 
from rotary_encoder import RotaryEncoder

class DrinksMachine:
    def __init__(self):
        self.database = Database()
        self.pumps = [
            Pump(pin=26), 
            Pump(pin=2), 
            Pump(pin=3), 
            Pump(pin=4),
        ]
        self.display = Display()
        self.rotery_encoder = RotaryEncoder()

        self.last_re_counter = self.rotery_encoder.counter()
    
    def destroy_pumps(self):
        for pump in self.pumps:
            pump.destroy()

    def update(self) -> None:
        self.rotery_encoder.update()

        new_re_counter = self.rotery_encoder.counter()
        if self.last_re_counter != new_re_counter:
            self.pumps[0].start(0.5)
            pass

    def run(self):
        while True:
            try:
                self.update()
            except Exception as e:
                self.destroy_pumps()
                self.rotery_encoder.destroy()
                print(e)
                break
            except KeyboardInterrupt:
                self.destroy_pumps()
                self.rotery_encoder.destroy()
                break


