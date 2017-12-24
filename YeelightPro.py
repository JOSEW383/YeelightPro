#!/usr/bin/python

import socket
from time import sleep

def operate_on_bulb(ip, method, params):
  port=55443
  try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Conectando con ",ip, port ,"..."
    tcp_socket.connect((ip, int(port)))

    msg2="{\"id\": 192.168.4.234, \"method\": \"set_rgb\", \"params\":[\"65280\", \"sudden\", 500]}\r\n"
    msg3="{\"id\": 192.168.4.234, \"method\": \"set_power\", \"params\":[\"off\", \"sudden\", 500]}\r\n"

    msg="{\"id\":" + str(ip) + ",\"method\":\""
    msg += method + "\",\"params\":[" + params + "]}\r\n"

    tcp_socket.send(msg)
    tcp_socket.close()
  except Exception as e:
    print "Ha habido un error:", e


def set_rgb(ip, color):
    operate_on_bulb(ip, "set_rgb", str(color))

def set_bright(ip, bright):
    operate_on_bulb(ip, "set_bright", str(bright))
    #effect (str)  The type of effect. Can be "smooth" or "sudden".

def set_color_temp(ip):
    operate_on_bulb(ip,"set_color_temp","")
    #Parameters:	degrees (int)  The degrees to set the color temperature to (1700 _ 6500).

def toggle(ip):
    operate_on_bulb(ip,"toggle","")

def turn_on(ip):
    params=["off","sudden",500]
    operate_on_bulb(ip,"set_power",params)

def turn_off(ip):
    params=["off", "sudden", 500]
    operate_on_bulb(ip,"set_power",params)

#MAIN DEL PROGRAMA DE LA BOMBILLA
print "Biemvenido al programa de YEELIGHT"

turn_off('192.168.4.234')
set_rgb('192.168.4.234', 16777215)

set_bright('192.168.4.234', 100)
sleep(0.5)
set_bright('192.168.4.234', 1)
sleep(0.5)
set_bright('192.168.4.234', 100)
sleep(0.5)
set_bright('192.168.4.234', 1)
sleep(0.5)
set_bright('192.168.4.234', 100)

#input("Pressione ENTER para continuar") #For view log
