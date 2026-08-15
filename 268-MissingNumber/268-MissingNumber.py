# Last updated: 8/15/2026, 3:05:45 PM
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        actual = n * (n+1) //2
        expected = sum(nums)
        return actual - expected
        