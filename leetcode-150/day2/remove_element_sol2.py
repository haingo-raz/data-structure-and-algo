# https://leetcode.com/problems/remove-element/solutions/5352400/python-100-beat-100-efficient-optimal-solution-easy-to-understand/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j