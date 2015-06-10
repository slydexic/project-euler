# Solution to Problem 7 in Project Euler.
# The answer is 104743. This program works!
# Initially, this program was very inefficient.
# However, I was able to make a more efficient program!

index = 3
trueOrFalse = []
primes = [2,3]

while len(primes) != 10001:

	for k in primes:
	
		if index % k == 0:
			trueOrFalse.append(False)
		
		else:
			trueOrFalse.append(True)
		
	if all(trueOrFalse) == True:
		primes.append(index)
		print index
	
	index = index + 2
	trueOrFalse = []

print "%d is the 10001st prime number!" % max(primes)