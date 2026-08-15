# Last updated: 8/15/2026, 3:05:28 PM
class Solution:
    def buildArray(self, target , n):
        operation = []
        for num in range(1,n+1):
            operation.append("Push")
            if num not in target:
                operation.append("Pop")
            if num == target[-1]:
                break
        return operation
        
