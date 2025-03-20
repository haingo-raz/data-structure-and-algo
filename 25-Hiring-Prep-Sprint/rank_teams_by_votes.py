# https://leetcode.com/problems/rank-teams-by-votes/
# https://leetcode.com/problems/rank-teams-by-votes/solutions/1429852/python-o-n-logn-solution-explained-easy-understanding/

# Example 1:
# Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
# Output: "ACB"
# Explanation: 
# Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
# Team B was ranked second by 2 voters and ranked third by 3 voters.
# Team C was ranked second by 3 voters and ranked third by 2 voters.
# As most of the voters ranked C second, team C is the second team, and team B is the third.

class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        # Dictionary to store the ranking count for each team
        team_rankings = {}

        # Iterate through each vote and record rankings
        for vote in votes:
            for position, team in enumerate(vote):
                # Initialize the ranking list for each team if not present
                if team not in team_rankings:
                    team_rankings[team] = [0] * len(vote)
                
                # Increment the count for the current ranking position
                team_rankings[team][position] += 1

        # Get a list of teams in alphabetical order
        team_list = sorted(team_rankings.keys())
        
        # Sort teams based on their ranking criteria
        # Primary: Most votes in higher positions
        # Secondary: Alphabetical order in case of tie
        return "".join(sorted(team_list, key=lambda team: team_rankings[team], reverse=True))
