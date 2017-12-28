#!/usr/bin/python

import re
import socket
from time import sleep

#-------------------------------------------------------------------------
#List of light bulbs
bulb1 = "192.168.5.110"
bulb2 = "192.168.5.111"
bulb3 = "192.168.5.112"
bulb4 = "192.168.5.113"

port=55443
#-------------------------------------------------------------------------
#Methods of yeelight

#TO DO
def get_param_value(data, param):


#info= power / bright / rgb
def get_info(ip,info):
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp_socket.settimeout(2)
	tcp_socket.connect((ip, int(port)))
	tcp_socket.send("{\"id\":" + ip + ", \"method\":\"get_prop\", \"params\":[\"power\", \"bright\", \"rgb\"]}\r\n")
	data = tcp_socket.recvfrom(2048)
	print data#FOR DEVELOPMENT!!!!!!!!!!!!!!
	tcp_socket.close()

	if info == "power":
		power = get_param_value(data,"power")
		return power
	elif info == "bright":
		bright = get_param_value(data,'bright')
		return bright
	elif info == "rgb":
		rgb = get_param_value(data,"rgb")
		return rgb
	else:
		return "error"

def operate_on_bulb(ip, method, params):
	try:
		tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp_socket.settimeout(2)
		print "Send to ",ip, port ,"..."
		tcp_socket.connect((ip, int(port)))

		#msg2="{\"id\": 192.168.4.234, \"method\": \"set_rgb\", \"params\":[\"65280\", \"sudden\", 500]}\r\n"

		msg="{\"id\":" + str(ip) + ",\"method\":\""
		msg += method + "\",\"params\":[" + params + "]}\r\n"

		tcp_socket.send(msg)
		tcp_socket.close()
	except Exception as e:
		print "An error has ocurred:", e

def set_rgb(ip, color):
    #white 16777215 blue 255 green 65280 red 16711680 pink 16711935 yellow 16776960 turquoise 65535
    params=",\"smooth\",500"
    operate_on_bulb(ip, "set_rgb", str(color)+params)

def set_bright(ip, bright):
    params=",\"smooth\",500"
    operate_on_bulb(ip, "set_bright", str(bright)+params)
    #effect (str)  The type of effect. Can be "smooth" or "sudden".
    #Minimun of bright is 1!!

def set_color_temp(ip):
    operate_on_bulb(ip,"set_color_temp","")
    #Parameters:	degrees (int)  The degrees to set the color temperature to (1700 _ 6500).

def toggle(ip):
    operate_on_bulb(ip,"toggle","")

def turn_on(ip):
    params="\"on\",\"smooth\",500"
    operate_on_bulb(ip,"set_power",params)

def turn_off(ip):
    params="\"off\",\"smooth\",500"
    operate_on_bulb(ip,"set_power",params)

#-------------------------------------------------------------------------
#Voids witch all light bulbs

def turn_on_all():
    turn_on(bulb1)
    turn_on(bulb2)
    turn_on(bulb3)
    turn_on(bulb4)

def turn_off_all():
    turn_off(bulb1)
    turn_off(bulb2)
    turn_off(bulb3)
    turn_off(bulb4)

#-------------------------------------------------------------------------
#Test

def test1():
    turn_off_all()
    turn_on(bulb4)
    set_rgb(bulb4, 16777215)
    for i in range(5):
        set_bright(bulb4, 1)
        sleep(0.5)
        set_bright(bulb4, 100)
        sleep(0.5)

def test2():
    turn_on_all()
    colors=[255,65280,16711680,16711935,16776960,65535]
    bulbs=[bulb1,bulb2,bulb3,bulb4]
    for i in range(4):
        set_bright(bulbs[i],100)
    for i in range(500):
        set_rgb(bulb1, colors[i%6])
        set_rgb(bulb2, colors[(i+1)%6])
        set_rgb(bulb3, colors[(i+2)%6])
        set_rgb(bulb4, colors[(i+3)%6])
        sleep(1)

def test3():
    turn_on_all()
    bulbs=[bulb1,bulb2,bulb3,bulb4]
    set_rgb(bulb1,16777215)
    set_rgb(bulb2,16777215)
    set_rgb(bulb3,16777215)
    set_rgb(bulb4,16777215)
    for i in range(4):
        set_bright(bulbs[i],1)
    for i in range(500):
        set_bright(bulbs[i%4],1)
        set_bright(bulbs[(i+1)%4],100)
        sleep(0.5)

def test4():
    turn_off_all()
    turn_on(bulb4)
    set_rgb(bulb4,9599999)
    set_bright(bulb4,50)

#-------------------------------------------------------------------------
#MAIN OF YEELIGHTPRO
print "Welcome to YeelightPro"
print get_info('192.168.5.113','power')
turn_off_all()
turn_on(bulb4)
set_rgb(bulb4, 16777215)
