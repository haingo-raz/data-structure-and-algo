class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        t = s.split()
        return map(pattern.find, pattern) == map(t.index, t) # Omitting parentheses (pattern.find) passes a function reference

        