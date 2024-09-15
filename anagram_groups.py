# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        listOfDictionaries = []
        for i in strs:
            listOfDictionaries.append([self.dictionarify(i), False])

        anagramsIndexes = {}

        for i in range(len(listOfDictionaries)):
            if listOfDictionaries[i][1]: continue

            anagramsIndexes[i] = [i]

            listOfDictionaries[i][1] = True

            for j in range(len(listOfDictionaries)):
                if listOfDictionaries[j][1]: continue

                same = True

                for entry in listOfDictionaries[i][0]:
                    if entry not in listOfDictionaries[j][0]:
                        same = False
                        break

                    if listOfDictionaries[i][0][entry] != listOfDictionaries[j][0][entry]:
                        same = False
                        break

                for entry in listOfDictionaries[j][0]:
                    if entry not in listOfDictionaries[i][0]:
                        same = False
                        break

                if same:
                    listOfDictionaries[j][1] = True
                    anagramsIndexes[i].append(j)

        print(anagramsIndexes)

        anagramsGrouped = []

        for entry in anagramsIndexes:
            stringArray = []
            for i in anagramsIndexes[entry]:
                string = strs[i]
                stringArray.append(string)
            anagramsGrouped.append(stringArray)

        return anagramsGrouped

    def dictionarify(self, inputStr: str) -> {}:
        dictionary = {}

        for i in inputStr:
            if i in dictionary:
                dictionary[i] += 1
                continue
            dictionary[i] = 1

        return dictionary