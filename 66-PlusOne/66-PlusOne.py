# Last updated: 9/2/2026, 5:52:34 PM
class Solution:
    def plusOne(self, digit):
        for i in range (len(digit)-1,-1,-1):
            if digit[i]<9:
                digit[i]+=1
                return digit
            digit[i]=0
        return [1]+digit
            