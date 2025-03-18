# https://leetcode.com/problems/valid-palindrome-ii/solutions/
# Solution: https://leetcode.com/problems/valid-palindrome-ii/solutions/209252/java-python-two-pointers-with-thinking-process/
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # If a mismatch occurs, check if removing either character results in a palindrome
                return self.validPalindromeUtil(s, i+1, j) or self.validPalindromeUtil(s, i, j-1)
        return True

    def validPalindromeUtil(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
