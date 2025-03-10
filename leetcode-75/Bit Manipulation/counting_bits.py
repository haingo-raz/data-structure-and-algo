# https://leetcode.com/problems/counting-bits/submissions/1569511201/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        counter = [0]
        for i in range(1, n +1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
        