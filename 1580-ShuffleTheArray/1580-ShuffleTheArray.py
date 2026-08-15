# Last updated: 8/15/2026, 3:05:30 PM
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        for i in range (n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
        