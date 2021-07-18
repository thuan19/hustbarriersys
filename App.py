from BarrierController import *

#State of the barrier: Up, Hold, or Down
barrier_state = "down"

while barrier_state != "stop":
    print("Enter the wanted state of the barrier: ", end = '')
    barrier_state = input()
    barrier_controller(barrier_state)

GPIO.cleanup()

