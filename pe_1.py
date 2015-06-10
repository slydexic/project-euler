# Solution to Problem 1 in Project Euler
# The answer is 233168. This program works!

theSet = range(1,1000)
multiplesOfFive = []
multiplesOfThree = []

for i in theSet:
    if i % 5 == 0:
	    multiplesOfFive.append(i)
    elif i % 3 == 0:
	    multiplesOfThree.append(i)

sumOfFives = sum(multiplesOfFive)
sumOfThrees = sum(multiplesOfThree)

totalSum = sumOfFives + sumOfThrees

print "The total sum is %d." % totalSum