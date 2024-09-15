# Given an integer array nums and an integer k, return the k most frequent elements within the array.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numDict = {}

        for i in nums:
            if i not in numDict:
                numDict[i] = [1, False]
                continue

            numDict[i][0] += 1

        unfinished = True
        result = []

        print(numDict)

        for i in range(k):
            greatest = None
            for i in numDict:
                if numDict[i][1]: continue
                if greatest is None:
                    greatest = i

                if numDict[i][0] > numDict[greatest][0]:
                    greatest = i

            result.append(greatest)
            numDict[greatest][1] = True

        return result