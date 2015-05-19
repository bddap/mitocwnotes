from math import *

def f(x):
	return 1/x

def fPrime(x,dx=0.00001):
	return (f(x+dx)-f(x))/dx

x=21.0
dx=1.0
while True:
	print("fPrime({0:.2f}".format(x) + ",{0:.30f}) = ".format(dx) + "-1.0/x^2 - {0:.50f}".format(-1.0/x**2 - fPrime(x,dx)))
	if fPrime(x,dx)==0:
		break	
	dx=dx*0.9999


