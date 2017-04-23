#!/usr/bin/python
# Author: Jon Trulson <jtrulson@ics.com>
# Copyright (c) 2015 Intel Corporation.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import print_function
import time, sys, signal, atexit, urllib, urllib2, math
from upm import pyupm_mpu9150 as sensorObj

def main():
	
#	data = {}
#	data['magnetrometro'] = raw_input(" Informe a temperatura")
	
#	data = urlib.urlencode(data)
#	post_request = urlib2.Request(post_url,data,headers)

#	try:
#		post_response = urlib2.urlopen(post_request)
#		print post_response.read()

#	except URLError as e:
#	print "Error: ", e.reason

    # Instantiate an MPU9250 on I2C bus 0
    sensor = sensorObj.MPU9250()

    ## Exit handlers ##
    # This function stops python from printing a stacktrace when you hit control-C
    def SIGINTHandler(signum, frame):
        raise SystemExit

    # This function lets you run code on exit
    def exitHandler():
        print("Exiting")
        sys.exit(0)

    # Register exit handlers
    atexit.register(exitHandler)
    signal.signal(signal.SIGINT, SIGINTHandler)

    sensor.init()

    x = sensorObj.new_floatp()
    y = sensorObj.new_floatp()
    z = sensorObj.new_floatp()

    while (1):

        sensor.update()
        sensor.getAccelerometer(x, y, z)

#        print ("Accelerometer: ")
#        print ("AX: %.4f" % sensorObj.floatp_value(x), end=' ')
#        print ("  AY: %.4f" % sensorObj.floatp_value(y), end=' ')
#        print ("  AZ: %.4f" % sensorObj.floatp_value(z))
        modulo1 = (sensorObj.floatp_value(x)-0.005)**2+(sensorObj.floatp_value(y)-0.0150)**2+(sensorObj.floatp_value(z)-0.0450)**2
#        print(modulo1)
        modulo1 = ("%.1f" % abs(((modulo1**0.5)-1)*9.8))
#        print (modulo1)


#
#        sensor.getGyroscope(x, y, z)
#        print("Gyroscope:     GX: ", sensorObj.floatp_value(x), end=' ')
#        print(" GY: ", sensorObj.floatp_value(y), end=' ')
#        print(" GZ: ", sensorObj.floatp_value(z))

        sensor.getMagnetometer(x, y, z)
#        print("Magnetometer:  MX: ", sensorObj.floatp_value(x), end=' ')
#        print(" MY: ", sensorObj.floatp_value(y), end=' ')
#        print(" MZ: ", sensorObj.floatp_value(z))
        modulo2 = sensorObj.floatp_value(x)**2+sensorObj.floatp_value(y)**2+sensorObj.floatp_value(z)**2
#        print(modulo2)
        modulo2 = ("%.2f" % (modulo2**0.5))
#        print (modulo2)

        arq = open('/tmp/dados.txt', 'w')
        texto = []
        texto.append(str(modulo2)+","+str(modulo1))
        arq.writelines(texto)
        arq.close()


#        link = ('http://data.sparkfun.com/input/0lwWlyRED5i7K0AZx4JO?private_key=D6v76yZrg9CM2DX8x97B&mag='+str(modulo2))
#        print ('enviando dados')
#        send = urllib2.urlopen(link)
#        page = send.read()
#        print (page)

#        link = ('http://data.sparkfun.com/input/1noGndywdjuDGAGd6m5K?private_key=0mwnmR9YRgSxApAo0gDX&acel='+str(modulo1))
#        print ('enviando dados')
#        send = urllib2.urlopen(link)
#        page = send.read()
#        print (page)

#        print("Temperature:  ", sensor.getTemperature())
#        print()

#        time.sleep(.5)

if __name__ == '__main__':
    main()