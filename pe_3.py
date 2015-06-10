# Solution to Problem 3 in project Euler
# The answer is 6857. This program works!
# Really proud of myself. This one was hard.

primeDivisors = []
index = 3
bigAssNumber = 600851475143
while index < bigAssNumber:
    if bigAssNumber % index == 0:
	   print "%d is a prime divisor." % index
	   primeDivisors.append(index)
	   bigAssNumber = bigAssNumber/index
	   print "Now checking index < %d" % bigAssNumber
    else:
	    pass
    index = index + 2
primeDivisors.append(bigAssNumber)

print "Done!"
print "All prime divisors found:"
print primeDivisors

print "The max prime divisor is %d." % max(primeDivisors)