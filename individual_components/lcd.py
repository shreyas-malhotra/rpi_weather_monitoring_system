# docs =  https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/

import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello World!", 1)