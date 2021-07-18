import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #Use GPIO pin-numbering, not generic
GPIO.setwarnings(False)

#Output to control the barrier
GPIO.setup(14, GPIO.OUT) #Up
GPIO.setup(15, GPIO.OUT) #Hold
GPIO.setup(18, GPIO.OUT) #Down

#State of the barrier: Up, Hold, or Down
def BarrierControl(status = "up"):
    print("The current state of the barrier:", status)

    if (status == "up"):
        GPIO.output(14, GPIO.LOW)
        time.sleep(0.5) #pusle = 0.3~0.5s to control the barrier
        GPIO.output(14, GPIO.HIGH)

    if (status == "hold"):
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(15, GPIO.HIGH)

    if (status == "down"):
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(18, GPIO.HIGH)