#from random import randint #<< For testing without use of serial
from sr import * #Don't know if it needs this to boot?
import serial
ser = serial.Serial('/dev/ttyACM0', 19200)

while True:
	x = ser.readline().strip
	#x = str(randint(0,255)) #<< For testing without use of serial
	try:
		print "Raw: " + str(x)
		x = int(x)
		print "Int: " + str(x)
		x = int(round((float(x) / 255) * 100))
		print "Adjusted: " + str(x)
		print "--------------"
	except ValueError:
		pass
