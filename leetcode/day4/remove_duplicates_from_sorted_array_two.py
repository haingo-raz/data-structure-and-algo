#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        for i in range(1, len(nums)):
            if j == 1 or nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j  


#j keeps track of the position where the next unique or allowed duplicate number should be placed.
#The loop starts from 1 instead of 0 because the first element doesn't need to be checked against anything before it.
#j == 1: If only one number has been processed, we can safely add the next one.      
#nums[i] != nums[j - 2]: Checks if the current number (nums[i]) is different from the second-to-last number in the modified list (nums[j-2]). If it's different, it's #safe to include the current number.
#If the condition is met, the current number is added to the list at position j.
#j is then increased by 1, moving to the next position for the next valid number.
#The function returns j, which represents the length of the modified list where each number appears at most twice.