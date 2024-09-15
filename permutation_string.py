# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Dict = {}
        for i in s1:
            s1Dict[i] = s1Dict.get(i, 0) + 1

        l = 0
        r = len(s1)

        substring = False

        for i in range(len(s2) - len(s1) + 1):
            substringDict = {}
            for i in s2[l:r]:
                substringDict[i] = substringDict.get(i, 0) + 1

            substring = True
            for i in s1Dict:
                if s1Dict[i] != substringDict.get(i, 0):
                    substring = False
                    break

            if substring: break

            l += 1
            r += 1

        return substring

