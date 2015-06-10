# Solution to Problem 6 in Project Euler.
# The answer is 25164150. This program works!
# This was an easy problem to solve.

sumOfSquares = 0
theSum = 0
for i in range(1,101):
    sumOfSquares = sumOfSquares + i*i
    theSum = i + theSum

print "The sum of squares from 1 to 100 is %d." % sumOfSquares
print "The sum from 1 to 100 is %d." % theSum

squareOfSum = theSum*theSum
difference = squareOfSum - sumOfSquares

print "The difference is %d." % difference