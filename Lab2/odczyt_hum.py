#!/usr/bin/env python3.6
path = "/sys/bus/iio/devices/iio:device0/in_humidityrelative_input"
with open(path,'r',encoding = 'utf-8') as f:
        print(f.read())  # read the entire file

