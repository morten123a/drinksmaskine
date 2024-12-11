from RPi import GPIO

class RotaryEncoder:
    def __init__(self):
        self.clk = 17
        self.dt = 18
        self.sw = 22
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.rawCounter = 0
        self.clkLastState = GPIO.input(self.clk)
    

    def update(self) -> None:
        clkState = GPIO.input(self.clk)
        dtState = GPIO.input(self.dt)
        if clkState != self.clkLastState:
            if dtState != clkState:
                self.rawCounter += 1
            else:
                self.rawCounter -= 1
            # print(self.rawCounter)
        self.clkLastState = clkState

    def has_rotated_clockwise(self) -> bool:
        return self.rawCounter <= -2

    def has_rotated_counter_clockwise(self) -> bool:
        return self.rawCounter >= 2

    def has_been_clicked(self) -> bool:
        return GPIO.input(self.sw) == GPIO.HIGH

    def reset(self):
        self.rawCounter = 0
    
    def destroy(self):
        GPIO.cleanup()
        





