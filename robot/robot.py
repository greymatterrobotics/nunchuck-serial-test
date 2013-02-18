from sr import *
import serial

ser = serial.Serial('/dev/ttyACM0', 19200)

print "Listening..."

while True:
	data = ser.readline().strip().split(',')
	data = [ int(x) for x in data ]
	print data