import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower() # Change all uppercase letters to lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s) # Remove non-alpha numeric character with regex
        opposite = s[::-1]
        if (s==opposite):
            return True
        else:
            return False
        

    def isPalindromeShorter(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        return s==s[::-1]
        
        