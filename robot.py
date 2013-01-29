#from random import randint #<< For testing without use of serial
from sr import * #Don't know if it needs this to boot?
import serial

ser = serial.Serial('/dev/ttyACM0', 19200)
last = ""

while True:
	x = ser.readline().strip
	#x = str(randint(0,255)) #<< For testing without use of serial
	try:
		if x != last: #Only print if the read value has changed (helps tidy up the log)
			last = x
			print "Raw: " + str(x)
			x = float(x) #Cast to float
			print "Float: " + str(x)
			x = int(round((x / 255) * 100)) #Do maths on float, round and cast back to int
			print "Adjusted Int: " + str(x)
			print "--------------"
	except ValueError:
		pass