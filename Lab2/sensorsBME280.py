#!/usr/bin/env python3.6
import paho.mqtt.client as mqtt
import time
import threading

def on_connect(client,userdata,flags, rc):
    print("Connected with result code "+str(rc))
    
def get_temp():
    path = "/sys/bus/iio/devices/iio:device0/in_temp_input"
    with open(path,'r',encoding = 'utf-8') as f:
        return (f.read())  # read the entire file

def get_pressure():
    path = "/sys/bus/iio/devices/iio:device0/in_pressure_input"
    with open(path,'r',encoding = 'utf-8') as f:
        return(f.read())  # read the entire file

def get_humidity():
    path = "/sys/bus/iio/devices/iio:device0/in_humidityrelative_input"
    with open(path,'r',encoding = 'utf-8') as f:
        return(f.read())  # read the entire file


client = mqtt.Client()
client.connect("localhost",1883,60)

while 1:
    client.publish("sensors/bme280/temp",get_temp().strip())
    client.publish("sensors/bme280/pres",get_pressure().strip())
    client.publish("sensors/bme280/hum",get_humidity().strip())
    time.sleep(5)


