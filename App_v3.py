from BarrierController import *

while True:
    print("Enter the registered license plate: ", end = '')
    licensePlate = input()
    if (licensePlate == "30A-12345"):
        status = 1
        BarrierControl(status)
    else:
        status = 0
        BarrierControl(status)
GPIO.cleanup()

