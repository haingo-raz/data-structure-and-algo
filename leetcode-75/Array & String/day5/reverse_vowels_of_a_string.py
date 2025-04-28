# Using two-pointers method.
# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert string to a list because strings are immutable in Python
        words = list(s)

        # Initialize two pointers: 
        start = 0  # Pointer starting from the beginning
        end = len(s) - 1  # Pointer starting from the end

        # Define the vowels (both uppercase and lowercase)
        vowels = "aeiouAEIOU"

        # Use two-pointer approach to swap vowels
        while start < end:
            # Move start forward if it's not a vowel
            while start < end and vowels.find(words[start]) == -1:
                start += 1

            # Move end backward if it's not a vowel
            while start < end and vowels.find(words[end]) == -1:
                end -= 1

            # Swap the vowels at start and end
            words[start], words[end] = words[end], words[start]

            # Move both pointers inward after swapping
            start += 1
            end -= 1

        # Convert the list back to a string and return the result
        return "".join(words)
