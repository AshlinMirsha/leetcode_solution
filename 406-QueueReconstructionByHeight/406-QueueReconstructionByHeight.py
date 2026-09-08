# Last updated: 9/8/2026, 9:44:29 AM
print("Ashlin Mirsha R K")
print("URK25CS1193")
class Solution:
    def reconstructQueue(self, people):
        # Step 1: Sort by height descending
        # If same height, sort k ascending
        people.sort(key=lambda x: (-x[0], x[1]))

        queue = []

        # Step 2: Insert each person at index k
        for person in people:
            queue.insert(person[1], person)

        return queue