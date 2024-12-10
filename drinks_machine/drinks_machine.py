from database import Database
from display import Display
from pump import Pump 
from rotary_encoder import RotaryEncoder
from time import sleep 

class DrinksMachine:
    def __init__(self):
        self.database = Database()
        self.pumps = [
            Pump(pin=26), 
        ]
        self.display = Display()
        self.rotary_encoder = RotaryEncoder()

        self.last_re_counter = self.rotary_encoder.counter()
    
    def destroy_pumps(self):
        for pump in self.pumps:
            pump.destroy()

    def update(self) -> None:
        self.rotary_encoder.update()

        new_re_counter = self.rotary_encoder.counter()
        if self.last_re_counter != new_re_counter:
            print(f"last: {self.last_re_counter}")
            print(f"new: {new_re_counter}")
            sleep(0.05)
            self.pumps[0].start(0.5)

    def run(self):
        while True:
            try:
                self.update()
            except Exception as e:
                print("shutting down gracefully...")
                self.destroy_pumps()
                self.rotary_encoder.destroy()
                print(e)
                break
            except KeyboardInterrupt:
                print("shutting down gracefully...")
                self.destroy_pumps()
                self.rotary_encoder.destroy()
                break


