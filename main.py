from machine import Pin, Timer
import machine
from time import sleep
import network
import dht


def turn_on_led(pin):
    led = Pin(pin, Pin.OUT)
    led.on()

def turn_off_led(pin):
    led = Pin(pin, Pin.OUT)
    led.off()



# pin definition
pin_power = 14
pin_wifi = 15
pin_dht22 = 22

# wifi connection
net_ssid = ""
net_password = ""

# sensor scan interval in seconds
dht_interval = 5



# power on
turn_on_led(pin_power)




# wifi not connected
turn_on_led(pin_wifi)

# connecting to wifi
while True:
    try:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(net_ssid, net_password)
        sleep(3)
        #print("status: " + str(wlan.status()))
        if False == wlan.isconnected():
            print('failed to connect to: ' + net_ssid)
        else:
            print('connected to :' + net_ssid)
            print(wlan.ifconfig())
            turn_off_led(pin_wifi)
            break
    except KeyboardInterrupt as e:
        print(e)
        turn_off_led(pin_power)
        turn_off_led(pin_wifi)
        machine.reset()



sensor = dht.DHT22(pin_dht22)

while 1:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        print("\n")
        print("temp: %3.1f " % temp)
        print("Hum: %3.1f %% " % hum)

        sleep(dht_interval)
    except OSError as e:
        print(e)
        sleep(1)
