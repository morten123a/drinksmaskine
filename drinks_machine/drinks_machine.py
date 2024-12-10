from database import Database
from display import Display
from pump import Pump 
from rotary_encoder import RotaryEncoder
from time import sleep 

class DrinksIdSelector:
    def __init__(self) -> None:
        self.current_id = 0

    def next_drink(self) -> None:
        self.current_id += 1
        if self.current_id > 10:
            self.current_id = 0

    def prev_drink(self) -> None:
        self.current_id -= 1
        if self.current_id < 0:
            self.current_id = 10

class DrinksMachine:
    def __init__(self):
        self.database = Database()
        self.pumps = [
            Pump(pin=26), 
        ]
        self.display = Display()
        self.rotary_encoder = RotaryEncoder()

        self.drinks_id_sel = DrinksIdSelector()

    def update(self) -> None:
        self.rotary_encoder.update()

        if self.rotary_encoder.has_rotated_clockwise():
            self.drinks_id_sel.next_drink()
            print("rotated clockwise")
            self.rotary_encoder.reset()
            print(f"current drink id = {self.drinks_id_sel.current_id}")
            
        if self.rotary_encoder.has_rotated_counter_clockwise():
            self.drinks_id_sel.prev_drink()
            print("rotated counter clockwise")
            self.rotary_encoder.reset()
            print(f"current drink id = {self.drinks_id_sel.current_id}")

    def destroy(self) -> None:
        self.destroy_pumps()
        self.rotary_encoder.destroy()

    def destroy_pumps(self):
        for pump in self.pumps:
            pump.destroy()

