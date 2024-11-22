# lcd docs =  https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/
import I2C_LCD_driver
import Adafruit_DHT as dht
from time import *
from gpiozero import InputDevice
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
DO_PIN = 13
GPIO.setup(DO_PIN, GPIO.IN)

mylcd = I2C_LCD_driver.lcd()

DHT_SENSOR = dht.DHT11
DHT_PIN= 4
no_rain = InputDevice(17)

while True:
    # Rain Sensor
    if not no_rain.is_active:
        print("Rain detected.")
    else:
        print("Rain not detected.")
        
    # DHT11
    humidity,temprature = dht.read_retry(DHT_SENSOR,DHT_PIN)
    if humidity is not None and temprature is not None:
        mylcd.lcd_display_string("Temp = {0:0.1f}*C".format(temprature), 1)
        mylcd.lcd_display_string("Humidity={0:0.1f}%".format(humidity), 2)
        sleep(2)
    else:
        print("Sensor malfunction.")
        
    #MQ2    
    gas_present = GPIO.input(DO_PIN)
    
    if gas_present == GPIO.LOW:
        gas_state = "Gas Present"
    else:
        gas_state = "No Gas"
 
    print("Gas State: ", gas_state)
 
    sleep(0.5)