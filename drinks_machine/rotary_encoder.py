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
        if clkState != clkLastState:
                if dtState != clkState:
                        self.rawCounter += 1
                else:
                        self.rawCounter -= 1
                print (self.rawCounter)
        clkLastState = clkState

    def counter(self) -> int:
          return self.rawCounter / 2




