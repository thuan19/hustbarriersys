import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #Use GPIO pin-numbering, not generic
GPIO.setwarnings(False)

#Output to control the barrier
GPIO.setup(14, GPIO.OUT) #Up
GPIO.setup(15, GPIO.OUT) #Hold
GPIO.setup(18, GPIO.OUT) #Down

#State of the barrier: Up, Hold, or Down
def barrier_controller(barrier_state = "up"):
    print("The current state of the barrier:", barrier_state)

    if (barrier_state == "up"):
        GPIO.output(14, GPIO.LOW)
        time.sleep(0.5) #pusle = 0.3~0.5s to control the barrier
        GPIO.output(14, GPIO.HIGH)

    if (barrier_state == "hold"):
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(15, GPIO.HIGH)

    if (barrier_state == "down"):
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(18, GPIO.HIGH)