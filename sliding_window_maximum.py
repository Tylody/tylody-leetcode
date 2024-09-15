# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = 0
        r = k

        result = []
        while True:
            if r == len(nums) + 1:
                break

            current_window = nums[l:r]
            result.append(max(current_window))

            print(current_window)

            l += 1
            r += 1

        return result
