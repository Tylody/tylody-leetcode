# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

class Solution:
    numbersDict = {}

    def crawlThrough(self, i: int) -> int:

        self.numbersDict[i] = False
        count = 1
        j = i

        while True:
            j = j + 1
            if j in self.numbersDict:
                count += 1
                self.numbersDict[j] = False
                print("\n" + str(i) + ", " + str(j))
                continue

            break

        j = i

        while True:
            j = j - 1
            if j in self.numbersDict:
                count += 1
                self.numbersDict[j] = False
                print("\n" + str(i) + ", " + str(j))
                continue

            break

        return count

    def longestConsecutive(self, nums: List[int]) -> int:

        self.numbersDict = {}

        for i in nums:
            self.numbersDict[i] = True
            print(str(i))

        greatestSequence = 0

        for i in self.numbersDict:
            if self.numbersDict[i]:
                new = self.crawlThrough(i)

                if new > greatestSequence:
                    greatestSequence = new

        return greatestSequence