// Taken from https://leetcode.com/problems/first-missing-positive/solutions/5694826/video-use-index-to-count-numbers/

class Solution {
    firstMissingPositive(nums) {
      // Step 1: Keep only positive numbers
      nums = nums.filter(n => n > 0);
  
      // Step 2: Use negative marking to indicate which numbers exist
      for (let n of nums) {
        const idx = Math.abs(n) - 1; // The index that represents the number n
        // If idx is within bounds and not already marked negative
        if (idx < nums.length && nums[idx] > 0) {
          nums[idx] *= -1; // Mark as present by making it negative
        }
      }
      
      // Step 3: The first index with a positive value means its number is missing
      for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 0) {
          return i + 1; // Return the missing positive integer
        }
      }
      
      // Step 4: If all positions are marked, return next integer
      return nums.length + 1;
    }
  }
  