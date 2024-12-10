from RPi import GPIO
from time import sleep

clk = 17
dt = 18
SW = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt)
                if clkState != clkLastState:
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print (counter)
                clkLastState = clkState
                sleep(0.01)
                if GPIO.input(SW) == GPIO.HIGH:
                    print("knap er trykket")
                    sleep(0.3)
                sleep(0.01)
except KeyboardInterrupt:
       print("Afslutter programmet")
       GPIO.cleanup()
finally:
        GPIO.cleanup()