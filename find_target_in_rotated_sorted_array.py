class Solution:
    length_array = None
    offset = None

    def search(self, nums, target):


        self.length_array = len(nums)

        self.offset = self.findMin(nums)

        start = 0
        end = self.length_array - 1

        print("\nlength_array: " + str(self.length_array) + "\noffset: " + str(self.offset))

        while start != end - 1:

            input()

            midpoint = (start + end) // 2

            print("\nstart: " + str(start) + "\nmidpoint: " + str(midpoint) + "\nadjusted_midpoint: " + str(self.adjust_index(midpoint)) + "\nend: " + str(end))

            if nums[self.adjust_index(midpoint)] == target:
                return self.adjust_index(midpoint)

            if nums[self.adjust_index(midpoint)] > target:
                end = midpoint

            if nums[self.adjust_index(midpoint)] < target:
                start = midpoint

        if nums[self.adjust_index(start)] == target:
            return self.adjust_index(start)

        if nums[self.adjust_index(end)] == target:
            return self.adjust_index(end)

        return -1

    def adjust_index(self, index):

        index += self.offset

        if index > self.length_array - 1:
            return index - self.length_array

        return index

    def reset_index(self, index: int) -> int:
        index -= self.offset

        if index < 0:
            return self.length_array + index

        return index

    def findMin(self, nums):

        minimum = float('inf')

        start = 0
        end = len(nums) - 1

        midpoint = (start + end) // 2

        while start != midpoint and end != midpoint:

            print("\nStart: " + str(start) + "\nMidpoint: " + str(midpoint) + "\nEnd: " + str(end) + "\nMin: " + str(
                minimum))

            if nums[midpoint] > nums[end]:
                start = midpoint
                minimum = min(minimum, nums[midpoint])

            if nums[midpoint] < nums[end]:
                end = midpoint
                minimum = min(minimum, nums[midpoint])

            midpoint = (start + end) // 2

        if nums[start] < nums[end]:
            return start
        if nums[end] < nums[start]:
            return end

mySolution = Solution()
print(mySolution.search([3,4,5,6,1,2], 1))