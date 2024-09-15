# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l = 0
        r = 1

        tDict = {}
        for i in t:
            tDict[i] = tDict.get(i, 0) + 1

        shortest_substring = None
        while True:

            if r == len(s) + 1:
                break

            if not self.check_if_contains(tDict, s[l:r]):
                r += 1
                continue

            temp_l = l
            while True:
                temp_l += 1
                new_string = s[temp_l:r]
                if self.check_if_contains(tDict, new_string):
                    continue
                l = temp_l - 1
                break

            temp_r = r
            while True:
                temp_r -= 1
                new_string = s[l:temp_r]
                if self.check_if_contains(tDict, new_string):
                    continue
                r = temp_r + 1
                break

            if shortest_substring is None:
                shortest_substring = s[l:r]
                l += 1
                continue

            if len(shortest_substring) > len(s[l:r]):
                shortest_substring = s[l:r]
                l += 1
                continue  # was continue

            else:
                l += 1
                continue

        if shortest_substring is None: return ""

        return shortest_substring

    def check_if_contains(self, tDict: dict, window: str) -> bool:
        contains_substring = True

        windowDict = {}
        for i in window:
            windowDict[i] = windowDict.get(i, 0) + 1

        for i in tDict:
            if windowDict.get(i, 0) < tDict[i]:
                contains_substring = False
                break

        return contains_substring
