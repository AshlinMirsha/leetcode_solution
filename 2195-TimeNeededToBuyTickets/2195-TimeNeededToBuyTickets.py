# Last updated: 9/2/2026, 6:11:02 PM
class Solution:
    def timeRequiredToBuy(self, tickets, k):
        time = 0

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)

        return time