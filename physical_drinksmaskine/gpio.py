# from RPi import GPIO
# from time import sleep
# import gpiod

# #This is testet and is working
# clk = 17
# dt = 18
# SW = 22
# PUMP1_PIN = 26

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# chip = gpiod.Chip('gpiochip4')
# led_line = chip.get_line(PUMP1_PIN)
# led_line.request(consumer="PUMP1", type=gpiod.LINE_REQ_DIR_OUT)

# counter = 0
# clkLastState = GPIO.input(clk)

# try:

#         while True:
#                 clkState = GPIO.input(clk)
#                 dtState = GPIO.input(dt)
#                 if clkState != clkLastState:
#                         if dtState != clkState:
#                                 counter += 0.5
#                         else:
#                                 counter -= 0.5
#                         print (counter)
#                 clkLastState = clkState
#                 sleep(0.05)
#                 if GPIO.input(SW) == GPIO.HIGH:
#                    print ("knap er trykket")
#                    led_line.set_value(1)
#                    sleep(0.5)
#                    led_line.set_value(0)
#                 sleep(0.01)
# except KeyboardInterrupt:
#         print("Afslutter programmet")
#         led_line.release()
#         GPIO.cleanup()


import gpiod
import time
sekunds = 3
LED_PIN = 26
chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
led_line.request(consumer="PUMP", type=gpiod.LINE_REQ_DIR_OUT)
try:
   
        led_line.set_value(1)
        time.sleep(sekunds)
        led_line.set_value(0)
        
finally:
   led_line.release()