# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            findNum = target - nums[i]

            for j in range(len(nums)):
                if i == j: continue
                if nums[j] == findNum:
                    return [i, j]
