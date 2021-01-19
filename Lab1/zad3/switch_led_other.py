#!/usr/bin/env python3.6
import paho.mqtt.client as mqtt
import time
import threading

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("gpio/488")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.payload, " --- ", str(msg.payload))
    if str(msg.payload) == "b'0'":
        ref_client.publish("led/504","0")
    else:
        ref_client.publish("led/504","1")

def on_message_ref(client, userdata, msg):
    print(msg.payload, " --- ", str(msg.payload))
    if str(msg.payload) == "b'0'":
        our_client.publish("led/504","0")
    else:
        our_client.publish("led/504","1")

ref_client = mqtt.Client()
ref_client.on_connect = on_connect
ref_client.on_message = on_message_ref
ref_client.connect("192.168.51.239", 1883, 60)

t1 = threading.Thread(target=ref_client.loop_forever)
t1.start()

our_client = mqtt.Client()
our_client.on_message = on_message
our_client.on_connect = on_connect
our_client.connect("localhost",1883,60)

t2 = threading.Thread(target=our_client.loop_forever)
t2.start()
