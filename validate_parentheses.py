# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:
#
#     Every open bracket is closed by the same type of close bracket.
#     Open brackets are closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Return true if s is a valid string, and false otherwise.

class Solution:

    def __init__(self):
        self.stack = []

    def isValid(self, s: str) -> bool:

        self.stack = []

        valid = True

        for i in s:
            if i == '[' or i == '{' or i == '(':
                self.push(i)

            if i == ']':
                val = self.pop()
                if val != '[':
                    valid = False
                    return valid

            if i == ')':
                val = self.pop()
                if val != '(':
                    valid = False
                    return valid

            if i == '}':
                val = self.pop()
                if val != '{':
                    valid = False
                    return valid

        if len(self.stack) != 0:
            valid = False

        return valid

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            return -1

        val = self.stack[-1]
        del self.stack[-1]
        return val
