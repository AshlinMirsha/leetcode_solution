# Last updated: 9/2/2026, 5:57:58 PM
class Solution:
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False

        peak = False
        up = False

        for i in range(len(arr) - 1):

            if not peak:
                if arr[i] < arr[i + 1]:
                    up = True

                elif arr[i] > arr[i + 1]:
                    if not up:
                        return False
                    peak = True

                else:
                    return False

            else:
                if arr[i] <= arr[i + 1]:
                    return False

        return peak