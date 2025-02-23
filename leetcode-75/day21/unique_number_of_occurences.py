# https://leetcode.com/problems/unique-number-of-occurrences/solutions/4577893/beats-100-users-c-java-python-javascript-2-approaches-explained/?envType=study-plan-v2&envId=leetcode-754
# The occurency are unique if the number of occurence is still the same after using set
# which means there were not duplicate values

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_dict = {}
        
        for el in arr:
            arr_dict[el] = arr_dict.get(el, 0) + 1
        return len(arr_dict) == len(set(arr_dict.values()))
    

        
            
            