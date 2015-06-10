# Solution to Problem 2 in Project Euler
# The answer is 4613732. This program works!

fibSet = []
evenFibSet = []
a = 0
b = 1

while b < 4000000:
    fibSet.append(b)
    a, b = b, a + b
	
for i in fibSet:
    if i % 2 == 0:
	    evenFibSet.append(i)
    else:
	    pass

totalSum = sum(evenFibSet)

print "The sum of even Fibonacci numbers below four million is %d." % totalSum