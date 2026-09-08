# Last updated: 9/8/2026, 5:49:07 PM
class Solution:
    def timeRequiredToBuy(self, tickets, k):
        time = 0

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)

        return time