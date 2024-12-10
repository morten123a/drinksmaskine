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

        # self.last_re_counter = self.rotary_encoder.counter()
    
    def destroy_pumps(self):
        for pump in self.pumps:
            pump.destroy()

    def update(self) -> None:
        self.rotary_encoder.update()

        if self.rotary_encoder.has_rotated_clockwise():
            print("rotated clockwise")
            self.rotary_encoder.reset()
            
        if self.rotary_encoder.has_rotated_counter_clockwise():
            print("rotated counter clockwise")
            self.rotary_encoder.reset()

        # new_re_counter = self.rotary_encoder.counter()
        # if abs(self.last_re_counter - new_re_counter) == 1:
        #     print(f"last: {self.last_re_counter}")
        #     print(f"new: {new_re_counter}")
        #     sleep(0.05)
        #     self.pumps[0].start(0.5)
        #     self.last_re_counter = new_re_counter

    def destroy(self) -> None:
        self.destroy_pumps()
        self.rotary_encoder.destroy()


