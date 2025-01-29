class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1 # Define two pointers which will be the start and end index of the nums array
        
        while left <= right: # As long as left is smaller or not equal to right i.e. the pointer didn't exceed the other one.
            mid = (left + right) // 2 # get the index of the middle element
            if nums[mid] == target: # return the index if it equals the target number
                return mid
            elif nums[mid] < target: # if the element is less than the target
                left = mid + 1 # The target must be on the right side of mid
            else:
                right = mid - 1 # The target must be on the lift side of mid
                
        return left # Else return the position of mid where the target would be placed if not found
        