from machine import Pin, Timer
from time import sleep
import network
import dht


def turn_on_led(pin):
    led = Pin(pin, Pin.OUT)
    led.on()




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
wifi_led = Pin(pin_wifi, Pin.OUT)
wifi_led_timer = Timer()

def blink_wifi_led(timer):
    wifi_led.toggle()

wifi_led_timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink_wifi_led)

# connecting to wifi
while True:
    try:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(net_ssid, net_password)

        if False == wlan.isconnected():
            print('failed to connect to: ' + net_ssid)
            sleep(1)
        else:
            print('connected to :' + net_ssid)
            wifi_led_timer.deinit()
            wifi_led.off()
            break
    except KeyboardInterrupt as e:
        print(e)
        sleep(2)



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
