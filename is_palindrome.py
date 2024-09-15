# Given a string s, return true if it is a palindrome, otherwise return false.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        stringBreakdown = s
        alphanumeric_only = ""

        for i in range(len(s)):
            if (stringBreakdown[0]).isalnum():
                print(stringBreakdown)
                alphanumeric_only = alphanumeric_only + stringBreakdown[0]

            if len(stringBreakdown) == 1:
                break

            stringBreakdown = stringBreakdown[1:]

        numberOfTests = len(alphanumeric_only) // 2
        print(alphanumeric_only)

        palindromic = True
        for i in range(numberOfTests):
            print("\n" + alphanumeric_only[i] + " + " + alphanumeric_only[-1 - i])
            if (alphanumeric_only[i]).upper() != (alphanumeric_only[-1 - i]).upper():
                palindromic = False
                break

        return palindromic

