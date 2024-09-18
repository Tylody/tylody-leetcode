class Solution:
    def findMin(self, nums) -> int:

        minimum = float('inf')

        start = 0
        end = len(nums) - 1

        midpoint = (start + end) // 2

        while start != midpoint and end != midpoint:

            print("\nStart: " + str(start) + "\nMidpoint: " + str(midpoint) + "\nEnd: " + str(end) + "\nMin: " + str(minimum))

            if nums[midpoint] > nums[end]:
                start = midpoint
                minimum = min(minimum, nums[midpoint])

            if nums[midpoint] < nums[end]:
                end = midpoint
                minimum = min(minimum, nums[midpoint])

            midpoint = (start + end) // 2

        return min(nums[start], nums[end])
