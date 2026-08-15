# Last updated: 8/15/2026, 3:05:38 PM
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        duplicate = 0
        missing = 0
        for num in nums:
            if num in seen:
                duplicate=num
            else:
                seen.add(num)
        for i in range(1,len(nums)+1):
            if i not in seen:
                missing = i
        return [duplicate, missing]
