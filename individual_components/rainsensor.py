# raindrop sensor DO connected to GPIO17
# HIGH = no rain, LOW = rain detected

from gpiozero import InputDevice
from time import sleep

no_rain = InputDevice(17)
 
while True:
    if not no_rain.is_active:
        print("It's raining - get the washing in!")
    else:
        print("No Rain :-(")
    sleep(1)