# https://leetcode.com/problems/longest-common-prefix/solutions/3273176/python3-c-java-19-ms-beats-99-91/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix=""
        strs = sorted(strs) # Sort the input to be able to compare the first and last item
        first=strs[0]
        last=strs[-1]
        #Iterate through the characters of the first and last string in the sorted list, stopping at the length of the shorter string
        for i in range(min(len(first), len(last))):
            if(first[i] != last[i]):
                return common_prefix
            common_prefix+=first[i]
        return common_prefix
        
        