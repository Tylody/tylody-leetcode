# You are given an integer array heights where heights[i] represents the height of the ith bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        greatest = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i == j: continue

                dist = abs(i - j)
                height = min(heights[i], heights[j])
                size = dist * height

                if size > greatest:
                    greatest = size

        return greatest