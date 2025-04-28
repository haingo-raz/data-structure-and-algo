class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = {}
        t_list = {}
        if len(s) == len(t):
            for char in s:
                # Count the occurence of each character in the string s
                # Init to 0 if not found in s_list, add 1 otherwise
                s_list[char] = s_list.get(char, 0) + 1

            for el in t:
                t_list[el] = t_list.get(el, 0) + 1

            # Compare exactly the two hash maps to check if they are similar
            return s_list == t_list


        # They cannot be anagrams if their length is not the same
        return False
        