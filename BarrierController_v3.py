import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #Use GPIO pin-numbering, not generic
GPIO.setwarnings(False)

#Output to control the barrier
GPIO.setup(14, GPIO.OUT) #Up
GPIO.setup(15, GPIO.OUT) #Down

#State of the barrier: Up or Down
def BarrierControl(status):
    if (status):
        GPIO.output(14, GPIO.LOW)
        time.sleep(0.5) #Open pusle = 0.3~0.5s to control the barrier
        GPIO.output(14, GPIO.HIGH)
        
        time.sleep(5)   #Hold for a few seconds before letting the barrier down
        
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.5) #Close pusle = 0.3~0.5s
        GPIO.output(15, GPIO.HIGH)

    else:
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.5) #Close pusle = 0.3~0.5s
        GPIO.output(15, GPIO.HIGH)