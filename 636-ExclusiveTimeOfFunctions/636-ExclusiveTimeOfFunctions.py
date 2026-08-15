# Last updated: 8/15/2026, 3:05:40 PM
class Solution:
    def exclusiveTime(self, n, logs):
        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            function_id, action, timestamp = log.split(":")
            
            function_id = int(function_id)
            timestamp = int(timestamp)

            if action == "start":
                # The function currently on top was running
                if stack:
                    result[stack[-1]] += timestamp - prev_time

                # Start the new function
                stack.append(function_id)

                # New starting point
                prev_time = timestamp

            else:
                # Current function runs until and including timestamp
                result[stack.pop()] += timestamp - prev_time + 1

                # Next function starts/resumes at timestamp + 1
                prev_time = timestamp + 1

        return result