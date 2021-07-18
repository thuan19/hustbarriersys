from BarrierController import *

#State of the barrier: Up, Hold, or Down
status = "down"

while status != "stop":
    print("Enter the wanted state of the barrier: ", end = '')
    status = input()
    BarrierControl(status)

GPIO.cleanup()

