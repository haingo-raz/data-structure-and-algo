# Binary search
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low <= high:
            guess_num = (low + high) // 2
            result = guess(guess_num)

            if result == -1:
                high = guess_num - 1 
            if result == 1:
                low = guess_num + 1
            if result == 0:
                return guess_num
