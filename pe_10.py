# Solution to Problem 10 in Project Euler

index = 3
trueOrFalse = []
primes = [2]
sumOfPrimes = 2

while max(primes) < 2000000:

	for k in primes:
	
		if index % k == 0:
			trueOrFalse.append(False)
		
		else:
			trueOrFalse.append(True)
		
	if all(trueOrFalse) == True:
		primes.append(index)
		print "%d is prime number %d." % (index, len(primes))
	
	trueOrFalse = []
	index = index + 2
	
print "The sum of all primes under 2,000,000 is %d." % sum(primes)