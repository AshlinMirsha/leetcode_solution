# Last updated: 9/25/2026, 7:07:37 PM
class Solution:
    def lastStoneWeight(self, stones):

        while len(stones) > 1:

            stones.sort()

            a = stones.pop()
            b = stones.pop()

            if a != b:
                stones.append(a - b)

        if len(stones) == 1:
            return stones[0]

        return 0