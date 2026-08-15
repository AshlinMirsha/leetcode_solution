# Last updated: 8/15/2026, 3:05:43 PM
class Solution(object):
    def findDisappearedNumbers(self, nums):
        seen = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in seen:
                result.append(i)

        return result