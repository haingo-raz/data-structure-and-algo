# Traverse through nums2 and append its elements to the end of nums1 starting from index m.
# Sort the entire nums1 array using sort() function.
# https://leetcode.com/problems/merge-sorted-array/solutions/3436053/beats-100-best-c-java-python-and-javascript-solution-two-pointer-stl/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def merge(self, nums1, m, nums2, n):
      for j in range(n):
          nums1[m+j] = nums2[j]
      nums1.sort()

solution = Solution()

# Define the inputs
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

# Call the merge method using the instance
solution.merge(nums1, m, nums2, n)

# Print the result
print(nums1)  # Output should be [1, 2, 2, 3, 5, 6]