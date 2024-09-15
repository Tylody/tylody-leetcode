#Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        result = []

        for i in range(len(numbers)):
            difference = target - numbers[i]
            print(str(difference))

            for j in range(len(numbers)):
                if numbers[j] == difference:
                    if numbers[i] > numbers[j]:
                        result = [j+1, i+1]
                    else:
                        result = [i+1, j+1]

                    return result
