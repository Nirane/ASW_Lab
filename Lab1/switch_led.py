#!/usr/bin/env python3.6
import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("gpio/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if str(msg.payload) == "b'0'":
        client.publish("led/504","0")
    else:
        client.publish("led/504","1")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

client.loop_forever()