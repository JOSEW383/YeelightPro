#!/usr/bin/python

import socket
from time import sleep

def operate_on_bulb(ip, method, params):
  port=55443
  try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Send to ",ip, port ,"..."
    tcp_socket.connect((ip, int(port)))

    msg2="{\"id\": 192.168.4.234, \"method\": \"set_rgb\", \"params\":[\"65280\", \"sudden\", 500]}\r\n"

    msg="{\"id\":" + str(ip) + ",\"method\":\""
    msg += method + "\",\"params\":[" + params + "]}\r\n"

    tcp_socket.send(msg)
    tcp_socket.close()
  except Exception as e:
    print "An error has ocurred:", e


def set_rgb(ip, color):
    operate_on_bulb(ip, "set_rgb", str(color))

def set_bright(ip, bright):
    params=",\"smooth\",500"
    operate_on_bulb(ip, "set_bright", str(bright)+params)
    #effect (str)  The type of effect. Can be "smooth" or "sudden".

def set_color_temp(ip):
    operate_on_bulb(ip,"set_color_temp","")
    #Parameters:	degrees (int)  The degrees to set the color temperature to (1700 _ 6500).

def toggle(ip):
    operate_on_bulb(ip,"toggle","")

def turn_on(ip):
    params="\"on\",\"sudden\",500"
    operate_on_bulb(ip,"set_power",params)

def turn_off(ip):
    params="\"off\",\"sudden\",500"
    operate_on_bulb(ip,"set_power",params)

#MAIN DEL PROGRAMA DE LA BOMBILLA
print "Welcome to YeelightPro"

turn_on('192.168.4.234')
#white 16777215 blue 255 green 65280 red 16711680 pink 16711935 yellow 16776960 turquoise 65535
set_rgb('192.168.4.234', 16777215)

for i in range(500):
    set_bright('192.168.4.234', 1)
    sleep(0.5)
    set_bright('192.168.4.234', 100)
    sleep(0.5)

#input("Press ENTER to continue") #For view log
