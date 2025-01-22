# https://leetcode.com/problems/valid-palindrome/solutions/3864359/python-3-two-solutions-beats-99-33ms/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))