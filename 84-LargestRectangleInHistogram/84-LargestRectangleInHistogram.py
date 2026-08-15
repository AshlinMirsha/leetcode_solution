# Last updated: 8/15/2026, 3:05:50 PM
class Solution:
    def largestRectangleArea(self, heights):

        heights.append(0)  # Add 0 here

        stack = []
        max_area = 0

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width

                max_area = max(max_area, area)

            stack.append(i)

        return max_area