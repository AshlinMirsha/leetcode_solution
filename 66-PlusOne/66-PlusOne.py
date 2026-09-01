# Last updated: 9/1/2026, 10:23:13 PM
class Solution:
    def plusOne(self,digit):
        for i in range (len(digit) -1 , -1, -1):
            if digit[i]<9:
                digit[i]+=1
                return digit
            digit[i]=0
        return[1]+digit

