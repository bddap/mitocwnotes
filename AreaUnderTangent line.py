import time

def curve(x):
	return 1.0/x

def curvePrime(x):
	return -1.0/(x**2)

def tangentLine(x):
	slope = curvePrime(x)
	x0 = x
	y0 = curve(x)
	return ((x0,y0),slope)	#defines a line

def yIntercept(line):
	((x0,y0),slope) = line
	return -slope*x0+y0

def xIntercept(line):
	((x0,y0),slope) = line
	return ((y0-slope*x0)/-slope)

def volumeOfTriangle(x):
	line = tangentLine(x)
	y = yIntercept(line)
	x = xIntercept(line)
	volume = x*y/2.0
	return volume

x = 0.01
while x < 5:
	tl = tangentLine(x)
	print ("tl(" + str(x) + ") = " + str(tl))
	print ("yIntercept(" + str(x) + ") = " + str(yIntercept(tl)))
	print ("xIntercept(" + str(x) + ") = " + str(xIntercept(tl)))
	print ("vt(" + str(x) + ") = " + str(volumeOfTriangle(x)))
	
	time.sleep(0.1)
	print("--------------------------------------------------")
	x = x + 0.01
