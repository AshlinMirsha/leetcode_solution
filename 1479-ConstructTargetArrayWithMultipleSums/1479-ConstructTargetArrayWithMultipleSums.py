# Last updated: 10/9/2026, 9:41:22 PM
import heapq

class Solution:
    def isPossible(self, target):
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)

        while True:
            largest = -heapq.heappop(heap)
            remaining = total - largest

            if largest == 1 or remaining == 1:
                return True

            if remaining == 0 or largest <= remaining:
                return False

            previous = largest % remaining

            if previous == 0:
                return False

            total = remaining + previous
            heapq.heappush(heap, -previous)