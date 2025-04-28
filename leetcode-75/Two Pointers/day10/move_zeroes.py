class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Tracks the position of where non-zero element should go
        non_zero_pos = 0

        # Iterate through the array
        for i in range(len(nums)):
            # When a non-zero element is found, swap the the position where it should go
            if nums[i] != 0:
                nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
                non_zero_pos += 1