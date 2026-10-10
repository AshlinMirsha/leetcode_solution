# Last updated: 10/10/2026, 9:25:11 PM
class Solution:
    def licenseKeyFormatting(self, s , k):
        s=s.replace("-","").upper()
        result = ""
        while len(s)>k:
            result = "-"+s[-k:]+result
            s = s[:-k]
        return s +result

        