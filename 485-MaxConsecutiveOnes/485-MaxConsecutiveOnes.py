# Last updated: 8/15/2026, 3:05:41 PM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maximum = 0
        for num in nums:
            if num == 1:
                count = count + 1
                maximum = max(maximum,count)
            else:
                count = 0
        return maximum      