#!/usr/bin/env python3.6
import paho.mqtt.client as mqtt
import time

import time
import gpio
import logging
print( "Test LED@PWM0\n")

#poziom logów
gpio.log.setLevel(logging.INFO)

#zmienne stanów
state = 0
last_state = 0

#ustawienie pinów w stan wejścia/wyjścia
#gpio.setup(504, gpio.OUT) #504/505
gpio.setup(488, gpio.IN)

client = mqtt.Client()
client.connect("localhost", 1883, 60)

#nasłuchiwanie zmian
while(True):
    state = gpio.read(488)

    if state != last_state and state:
        client.publish("gpio/488","1")
        #gpio.set(504,1)
        print("Włączanie diody")
    elif state != last_state and state == 0:
        client.publish("gpio/488","0")
        #gpio.set(504,0)
        print("Wyłączanie diody")

    last_state = state

    time.sleep(0.5)
