#Not optimal 
#Sliding" the needle over the haystack

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)

        # Iterate through the haystack
        for i in range(n - m + 1):
            # Check if substring matches needle
            if haystack[i:i + m] == needle:
                return i
        
        return -1