from machine import Pin
from time import sleep
import dht

sensor = dht.DHT22(Pin(22))

print("init ...")

try:
  sensor.measure()
  temp = sensor.temperature()
  hum = sensor.humidity()

  print("temp: %3.1f " %temp)
  print("Hum: %3.1f %% " %hum)
except OSError as e:
  print("error")