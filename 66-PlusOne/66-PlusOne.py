# Last updated: 8/15/2026, 3:05:53 PM
class Solution:
    def plusOne(self, digits):

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits