#https://leetcode.com/problems/maximum-average-subarray-i/solutions/3532127/py3-beginner-friendly-with-details-and-explanation/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Initializing the current sum and max sum to the sym of the initial k element of the list
        currentSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):

            currentSum += nums[i] - nums[i-k]
            maxSum = max(maxSum, currentSum)
        
        return maxSum/float(k)
        