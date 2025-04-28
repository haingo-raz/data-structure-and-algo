class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        res = []

        # Loop as long as the pointer has not gone through a whole word yet
        while i < len(word1) and i < len(word2):
            res.append(word1[i])
            res.append(word2[i])
            i += 1

        # Append the remaining characters to the result
        res.append(word1[i:])
        res.append(word2[i:])

        return ''.join(res)