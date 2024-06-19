from machine import Pin
from time import sleep
import dht

# pin definition
pin_power = 0
pin_network = 1
pin_dht22 = 22

sensor = dht.DHT22(pin_dht22)

while 1:
    try:
      sensor.measure()
      temp = sensor.temperature()
      hum = sensor.humidity()

      print("\n")
      print("temp: %3.1f " %temp)
      print("Hum: %3.1f %% " %hum)
      
      sleep(3)
    except OSError as e:
      print(e)
      sleep(1)
