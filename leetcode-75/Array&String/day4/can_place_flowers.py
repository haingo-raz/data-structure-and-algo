# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]  # The list representing the flowerbed (0 = empty, 1 = occupied)
        :type n: int  # The number of flowers to plant
        :rtype: bool  # Returns True if we can plant all 'n' flowers, otherwise False
        """

        # If no flowers need to be planted, return True immediately
        if n == 0:
            return True

        # Iterate through the flowerbed to find places to plant flowers
        for i in range(len(flowerbed)):
            
            # Check if the current plot is empty and both left and right plots are also empty (or boundaries)
            if (flowerbed[i] == 0 and  # Current plot is empty
                (i == 0 or flowerbed[i-1] == 0) and  # Either it's the first plot or the left plot is empty
                (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):  # Either it's the last plot or the right plot is empty
                
                # Plant a flower at position i
                flowerbed[i] = 1
                # Reduce the count of flowers we need to plant
                n -= 1

                # If all flowers are planted, return True immediately
                if n == 0:
                    return True

        # If we exit the loop and still have flowers left to plant, return False
        return False
