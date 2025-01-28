# https://leetcode.com/problems/happy-number/solutions/843860/python-3-tortoise-hare-technique/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
        slow = self.squared(n)
        fast = self.squared(self.squared(n))

        while slow!=fast and fast!=1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))

        return fast==1

    def squared(self, n):
        result = 0
        while n>0:
            last = n%10
            result += last * last
            n = n//10
        return result