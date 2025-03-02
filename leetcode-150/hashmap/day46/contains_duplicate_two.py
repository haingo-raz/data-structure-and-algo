class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_indices = {}  # Dictionary to store the last seen index of each number
    
        for i, num in enumerate(nums):
            if num in num_indices and i - num_indices[num] <= k:
                return True  # Found a duplicate within the required index range
            num_indices[num] = i  # Update the last seen index of the number
        
        return False

        