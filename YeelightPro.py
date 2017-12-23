#!/usr/bin/python

import socket
from time import sleep

def operate_on_bulb(ip, method, params):

  bulb_ip='192.168.4.234'
  port=55443
  try:
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Conectando con ",bulb_ip, port ,"..."
    tcp_socket.connect((bulb_ip, int(port)))

    msg2="{\"id\": 192.168.4.234, \"method\": \"set_rgb\", \"params\":[\"65280\", \"smooth\", 500]}\r\n"

    msg="{\"id\":" + str(bulb_ip) + ",\"method\":\""
    msg += method + "\",\"params\":[" + params + "]}\r\n"

    tcp_socket.send(msg)
    tcp_socket.close()
  except Exception as e:
    print "Ha habido un error:", e


def set_rgb(idx, color):
  operate_on_bulb(idx, "set_rgb", str(color))

def set_bright(idx, bright):
  operate_on_bulb(idx, "set_bright", str(bright))


#MAIN DEL PROGRAMA DE LA BOMBILLA
print "Biemvenido al programa de YEELIGHT"
print "Cargando configuracion..."

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
input("Pressione ENTER para continuar")
