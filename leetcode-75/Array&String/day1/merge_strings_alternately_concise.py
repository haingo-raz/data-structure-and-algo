class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        return ''.join(a + b for a, b in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):]
