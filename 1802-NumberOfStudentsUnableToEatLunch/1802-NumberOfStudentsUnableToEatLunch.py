# Last updated: 8/15/2026, 3:05:27 PM
class Solution:
    def countStudents(self,students,sandwitches):
        count=[0,0]
        for student in students:
            count[student]+=1
        for sandwitch in sandwitches:
            if count[sandwitch] == 0:
                break
            count[sandwitch]-=1
        return count[0]+count[1]
students=[1,0,1,0,1,0]
sandwitches=[0,1,0,1,1,0]
solution = Solution()
print(solution.countStudents(students,sandwitches))