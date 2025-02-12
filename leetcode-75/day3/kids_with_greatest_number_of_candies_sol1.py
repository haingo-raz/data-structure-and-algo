#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/solutions/3425582/easy-solutions-in-java-python-and-c-look-at-once-with-exaplanation/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        result = []

        for candy in candies: 
            result.append(candy + extraCandies >= max_candies)
        return result