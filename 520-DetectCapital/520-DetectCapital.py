# Last updated: 10/9/2026, 9:50:57 PM
class Solution:
    def detectCapitalUse(self, word):
        if word.isupper() or word.islower() or word.istitle():
            return True
        else:
            return False
        