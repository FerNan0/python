from _future_ import print_function

import time, sys, signal, atexit, urllib, urllib2, math

from upm import pyupm_mpu9150 as sensorObj

def main():

sensor = sensorObj.MPU9250()

def SIGINTHandler(signum, frame):

raise SystemExit

def exitHandler():

print("Exiting")

sys.exit(0)

atexit.register(exitHandler)

signal.signal(signal.SIGINT, SIGINTHandler)

sensor.init()

x = sensorObj.new_floatp()

y = sensorObj.new_floatp()

z = sensorObj.new_floatp()

while (1):

sensor.update()

sensor.getAccelerometer(x, y, z)

modulo1 = (sensorObj.floatp_value(x)-0.005)*2+(sensorObj.floatp_value(y)-0.0150)2+(sensorObj.floatp_value(z)-0.0450)*2

modulo1 = ("%.1f" % abs(((modulo1**0.5)-1)*9.8))

sensor.getMagnetometer(x, y, z)

modulo2 = sensorObj.floatp_value(x)*2+sensorObj.floatp_value(y)2+sensorObj.floatp_value(z)*2

modulo2 = ("%.2f" % (modulo2**0.5))

arq = open('/tmp/dados.txt', 'w')

texto = []

texto.append(str(modulo2)+","+str(modulo1))

arq.writelines(texto)

arq.close()


if _name_ == '_main_':

main()
