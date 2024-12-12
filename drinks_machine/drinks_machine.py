from database import Database
from display import Display
from pump import Pump 
from rotary_encoder import RotaryEncoder
from time import sleep 

class DrinksIdSelector:
    def __init__(self) -> None:
        self.current_id = 0
        self.min_id = 0
        self.max_id = 10

    def next_drink(self) -> None:
        self.current_id += 1
        if self.current_id > self.max_id:
            self.current_id = self.min_id

    def prev_drink(self) -> None:
        self.current_id -= 1
        if self.current_id < self.min_id:
            self.current_id = self.max_id

    def set_max_id(self, id) -> None:
        self.max_id = id - 1

    # def get_current_id_Write_display(self):
    #     print(f"current drink = {self.database.current_available_drinks([self.drinks_id_sel.current_id]["name"])}")
    #     self.drink_name = self.database.current_available_drinks([self.drinks_id_sel.current_id]["name"])
    #     self.display.write_ingredients_on_screen(self.drink_name,self.drinks_id_sel.current_id)
   



class DrinksMachine:
    def __init__(self):
        self.database = Database()
        self.pumps = [
            Pump(pin=26), 
            Pump(pin=16), 
            Pump(pin=19), 
            Pump(pin=13), 
        ]
        self.display = Display()
        self.rotary_encoder = RotaryEncoder()

        self.drinks_id_sel = DrinksIdSelector()

        self.database.connect_db()
        self.drinks_id_sel.set_max_id(self.database.max_value())

    def update(self) -> None:
        self.rotary_encoder.update()

        if self.rotary_encoder.has_rotated_clockwise():
            self.drinks_id_sel.next_drink()
            print("rotated clockwise")
            self.rotary_encoder.reset()
            self.get_current_id_Write_display()

        if self.rotary_encoder.has_rotated_counter_clockwise():
            self.drinks_id_sel.prev_drink()
            print("rotated counter clockwise")
            self.rotary_encoder.reset()
            self.get_current_id_Write_display()
        
        if self.rotary_encoder.has_been_clicked():
            self.dispense()
    
    def get_current_id_Write_display(self):
        #print(f"current drink = {self.database.current_available_drinks([self.drinks_id_sel.current_id]["name"])}")
        available_drinks = self.database.current_available_drinks()
        self.drink_name = available_drinks[self.drinks_id_sel.current_id]["name"]
        print(self.drink_name)
        self.display.write_ingredients_on_screen(self.drink_name,self.drinks_id_sel.current_id)

    def dispense(self):
        #vide hvor meget den skal pumpe
        for ingredient in self.database.current_available_drinks()[self.drinks_id_sel.current_id]["ingredients"]:
            number_of_ingredient = 0
            self.amount = self.database.current_available_drinks()[self.drinks_id_sel.current_id]["ingredients"][number_of_ingredient]['name']
            self.subtraction = self.database.subtract_poured_amount(ingredient, self.amount)
            match ingredient:
                case 'gin':
                    self.pumps[0].start(self.amount)
                    self.subtraction
                    
                case 'mango sirup':
                    self.pumps[1].start(self.amount)
                    self.subtraction

                case 'vodka':
                    self.pumps[2].start(self.amount)
                    self.subtraction

                case 'likoer43': 
                    self.pumps[3].start(self.amount)
                    self.subtraction

                case _:
                    self.display.get_extra_drink(ingredient, self.amount)
                    self.subtraction
            number_of_ingredient += 1
        #sende informationen til den rigtige pumpe x
        #?status på display? x
        #fjern mængden fra databasen

    def destroy(self) -> None:
        self.destroy_pumps()
        self.rotary_encoder.destroy()
        self.display.destroy()

    def destroy_pumps(self):
        for pump in self.pumps:
            pump.destroy()

