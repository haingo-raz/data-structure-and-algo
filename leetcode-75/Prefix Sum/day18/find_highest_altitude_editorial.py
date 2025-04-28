class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude = 0 # Define the starting point
        highest_point = current_altitude # Keeping track of the highest altitude

        for altitude_gain in gain: # Get the real altitude values
            current_altitude += altitude_gain
            highest_point = max(highest_point, current_altitude) #Iteratively compare the current altitude to the previous altitude
        
        return highest_point
        