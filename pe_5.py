# Solution to Problem 5 in Project Euler.
# The answer is 232792560. This program works!
# I forgot how I figured this out.

index = 19*17*13*11*7*5*3*2

while ((index % 1 != 0) or (index % 2 != 0) or (index % 3 != 0) or
      (index % 4 != 0) or (index % 5 != 0) or (index % 6 != 0) or
      (index % 7 != 0) or (index % 8 != 0) or (index % 9 != 0) or
	  (index % 10 != 0) or (index % 11 != 0) or (index % 12 != 0) or
	  (index % 13 != 0) or (index % 14 != 0) or (index % 15 != 0) or
	  (index % 16 != 0) or (index % 17 != 0) or (index % 18 != 0) or
	  (index % 19 != 0) or (index % 20 != 0)):
	  
	  print index
	  index = index + (19*17*13*11*7*5*3*2)

print "The answer is %d." % index