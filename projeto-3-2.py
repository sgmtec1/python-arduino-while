from pyfirmata import Arduino, util
import time
board=Arduino ('COM6')

while True:
    board.digital[7].write(1)
    time.sleep(0.5)
    board.digital[7].write(0)
    time.sleep(0.5)