
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = {}

        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                for k in range(len(nums) - i - j - 2):

                    if nums[i] + nums[j + i + 1] + nums[k + i + j + 2] == 0:

                        output = [nums[i], nums[j + i + 1], nums[k + i + j + 2]]
                        output.sort()

                        stringify = str(output[0]) + ' ' + str(output[1]) + ' ' + str(output[2])

                        if stringify in result:
                            continue

                        result[stringify] = True

        arrayOutput = []

        for i in result:
            process = i.split()
            intOutput = [int(process[0]), int(process[1]), int(process[2])]
            arrayOutput.append(intOutput)

        return arrayOutput