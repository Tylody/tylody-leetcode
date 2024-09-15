# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zeroes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes.append(i)

        if len(zeroes) > 1:
            return [0 for i in range(len(nums))]

        if len(zeroes) == 1:
            output = [0 for i in range(len(nums))]

            product = 1
            for i in range(len(nums)):
                if i == zeroes[0]:
                    continue

                product = product * nums[i]

            output[zeroes[0]] = int(product)

            return output

        product = 1
        output = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            product = product * nums[i]

        for i in range(len(nums)):
            output[i] = int(product / nums[i])

        return output