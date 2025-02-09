# https://leetcode.com/problems/guess-number-higher-or-lower/solutions/1001510/python-beats-99-solutions-o-log-n-w-comments-and-using-walrus-operator/?envType=study-plan-v2&envId=leetcode-75
# Binary search
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

def guessNumber(self, n: int) -> int:
	lowerBound, upperBound = 1, n
	# Binary division faster than (lowerBound + upperBound) //2
	myGuess = (lowerBound+upperBound) >> 1 # The shift >> 1 is mathematically equivalent to dividing by 2 with integer division (// 2)
	# walrus operator ':=' - assigns value of the function to the variable 'res'
	# and then compare res with 0
	while (res := guess(myGuess)) != 0:
		if res == 1:
			lowerBound = myGuess+1
		else:
			upperBound = myGuess-1
		myGuess = (lowerBound+upperBound) >> 1

	return myGuess