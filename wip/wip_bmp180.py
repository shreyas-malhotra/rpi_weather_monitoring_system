import Adafruit_BMP.BMP085 as BMP085
sensor = BMP085.BMP085()
print('Pressure={0:0.2f} Pa'.format(sensor.read_pressure()))
print('Altitude={0:0.2f} m'.format(sensor.read_altitude()))
print('Pressure={0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))      