#https://leetcode.com/problems/majority-element/solutions/3676530/3-method-s-beats-100-c-java-python-beginner-friendly/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        return nums[n//2]
            
# The intuition behind this approach is that if an element occurs more than n/2 times in the array
# (where n is the size of the array), it will always occupy the middle position when the array is sorted. 
# Therefore, we can sort the array and return the element at index n/2.