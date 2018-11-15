import random
import math



def CalcoloVolume(r):
	V=4/3*math.pi*r**3
	return V


# main
r=random.randrange(0,21)
print("Raggio:", r)
V=CalcoloVolume(r)
print("Volume:", V)