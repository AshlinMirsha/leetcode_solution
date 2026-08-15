# Last updated: 8/15/2026, 3:05:34 PM
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = []

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)

        return result