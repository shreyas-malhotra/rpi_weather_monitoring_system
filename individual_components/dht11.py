import Adafruit_DHT as dht
from time import sleep
DHT_SENSOR = dht.DHT11
DHT_PIN= 13
while True:
	humidity,temprature = dht.read_retry(DHT_SENSOR,DHT_PIN)
	if humidity is not None and temprature is not None:
		print("Temp = {0:0.1f}*C Humidity={1:0.1f}%".format(temprature,humidity))
		sleep(3)
	else:
		print("Sensor Failiure")
