# Last updated: 8/15/2026, 3:05:44 PM
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left = 0
        right=n
        while left <= right:
            mid = (left +right)//2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left