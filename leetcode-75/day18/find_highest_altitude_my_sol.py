class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        start_point = 0 # Define the starting point
        altitudes = [] # Create an list that will hold the real altitude points
        for i in gain: # Get the real altitude values
            start_point += i
            altitudes.append(start_point) # Save each computation into the list
        if max(altitudes)<= 0: # Return 0 if it's the max value or other values are below 0
            return 0
        return max(altitudes) # Else return the highest value
        