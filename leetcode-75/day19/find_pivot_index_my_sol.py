# Bad runtime

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]): # O(n²) time complexity
                return i
            elif sum(nums[:i]) == 0 and sum(nums[i+1:]) == 0:
                return 0
        return -1