# Last updated: 8/15/2026, 3:05:36 PM
class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
        return -1

        