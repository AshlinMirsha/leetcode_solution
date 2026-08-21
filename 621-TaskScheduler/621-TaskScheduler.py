# Last updated: 8/21/2026, 3:02:42 PM
print("Ashlin Mirsha R K")
print("URK25CS1193")
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)

        max_freq = max(freq.values())

        max_count = list(freq.values()).count(max_freq)

        result = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), result)