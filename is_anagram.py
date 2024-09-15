# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = self.tally_letters(s)
        t_dict = self.tally_letters(t)

        for s in s_dict:
            if s in t_dict:
                if s_dict[s] == t_dict[s]:
                    continue
            return False

        for t in t_dict:
            if t in s_dict:
                if t_dict[t] == s_dict[t]:
                    continue
            return False

        return True

    def tally_letters(self, s: str) -> {}:
        dictionary = {}

        for i in s:
            if i not in dictionary:
                dictionary[i] = 1
                continue

            dictionary[i] = dictionary[i] + 1

        print(dictionary)
        return dictionary