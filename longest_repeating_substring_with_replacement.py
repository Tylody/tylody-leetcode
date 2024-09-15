# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 1

        greatest = 0

        while True:
            charDict = {}
            for i in range(l, r):
                # increment charDict entry by 1, or initialize
                print(str(i))
                charDict[s[i]] = charDict.get(s[i], 0) + 1

            most_common_character = s[l]
            for i in charDict:
                if charDict[i] > charDict[most_common_character]:
                    most_common_character = i

            other_character_count = 0
            for i in charDict:
                if i == most_common_character: continue
                other_character_count += charDict[i]

            if other_character_count > k:
                l += 1
                continue

            r += 1

            addon = min(other_character_count, k)

            if charDict[most_common_character] + addon > greatest:
                greatest = charDict[most_common_character] + addon

            if r == len(s) + 1:
                print('right: ' + str(r) + '\nleft: ' + str(l) + '\ndict: ')
                print(charDict)
                break

        return greatest
