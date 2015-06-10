# Solution to Problem 4 in Project Euler
# The answer is 906609 = 993*913. This program works!
palindromeDigits = []
possiblePalindromes = {}

for row in range(900, 1000):
    for column in range(900, 1000):
        number = row * column
        palindromeDigits = list(str(number))
        if palindromeDigits == palindromeDigits[::-1]:
	        possiblePalindromes[number] = "%d * %d" % (row, column)
        else:
		    print palindromeDigits
		    print "%d is not a palindrome" % number

print "Search completed."
print "The palindromes are:"
print possiblePalindromes

print max(possiblePalindromes), " is the largest palindrome"
print "with the 3x3 product ", possiblePalindromes[max(possiblePalindromes)], "."