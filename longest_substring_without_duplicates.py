# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        greatest_substring = 0

        for i in range(len(s)):
            current_index = i
            tally = 1
            found_chars = {}
            found_chars[s[current_index]] = True

            while True:
                current_index += 1
                if current_index >= len(s):
                    break
                if s[current_index] in found_chars:
                    break
                found_chars[s[current_index]] = True
                tally += 1
                continue

            current_index = i

            while True:
                current_index -= 1
                if current_index <= -1:
                    break
                if s[current_index] in found_chars:
                    break
                found_chars[s[current_index]] = True
                tally += 1
                continue

            if tally > greatest_substring:
                greatest_substring = tally

        return greatest_substring


