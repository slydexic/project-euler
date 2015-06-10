# Solution to Problem 9 in Project Euler
# The answer is 31875000. This program works!

import math

triplets = []

for b in range(3,400):
    for a in range (1,b):
        c = math.sqrt(a*a + b*b)
        if a + b + c == 1000:
            triplets.append(a)
            triplets.append(b)
            triplets.append(int(c))

        else:
		    print "%d,%d,%d are not triplets" % (a,b,c)
			
print triplets
product = int(triplets[0]*triplets[1]*triplets[2])

print product