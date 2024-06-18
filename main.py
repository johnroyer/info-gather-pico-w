from machine import Pin
from time import sleep
import dht

sensor = dht.DHT22(Pin(22))

print("init ...")

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
      print("error")
