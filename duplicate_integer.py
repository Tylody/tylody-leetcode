# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         dictionary = {}

         for i in nums:
            if i in dictionary:
                return True
            dictionary[i] = True

         return False