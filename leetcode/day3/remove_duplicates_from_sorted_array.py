#https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        return len(nums)


# set(nums) converts the list into a set, which automatically removes all duplicate values.
# sorted(...) converts the set back into a sorted list.
# nums[:] = ... modifies the original list nums in place using slice assignment. It replaces all elements in nums with the sorted, duplicate-free elements.
# When used in an assignment (nums[:] = ...), it replaces all elements of the list with the elements from the right side of the assignment.
