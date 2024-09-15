# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        listChars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        for string in strs:

            length = len(string)

            if string == "":
                encoded = encoded + "0"
                continue

            if (string[0]).isdigit():
                length_as_letters = ""
                length_as_string = str(length)

                while length_as_string != "":
                    encoded = encoded + listChars[int(length_as_string[0])]

                    if len(length_as_string) > 1:
                        length_as_string = length_as_string[1:]
                    else:
                        length_as_string = ""

                encoded = encoded + string

                continue

            encoded = encoded + str(length)
            encoded = encoded + string

        print(encoded)

        return encoded

    def decode(self, s: str) -> List[str]:

        letters = {"A": "0", "B": "1", "C": "2", "D": "3", "E": "4", "F": "5", "G": "6", "H": "7", "I": "8", "J": "9"}

        fullStrings = []

        stringBreakdown = s

        while len(stringBreakdown) != 0:

            print(stringBreakdown)

            if (stringBreakdown[0]) == "0":
                fullStrings.append("")
                newString = stringBreakdown[1:]
                stringBreakdown = newString
                continue

            if (stringBreakdown[0]).isupper():
                length = ""

                while True:
                    if (stringBreakdown[0]).isupper():
                        length = length + letters[stringBreakdown[0]]
                        newString = stringBreakdown[1:]
                        stringBreakdown = newString
                        continue

                    break

                print("\n" + length)

                if length == "":
                    break

                lengthInt = int(length)
                inputString = stringBreakdown[:lengthInt]
                fullStrings.append(inputString)

                newString = stringBreakdown[lengthInt:]
                stringBreakdown = newString

                continue

            length = ""
            while True:
                if (stringBreakdown[0]).isdigit():
                    length = length + stringBreakdown[0]
                    newString = stringBreakdown[1:]
                    stringBreakdown = newString
                    continue

                break

            print('\n' + length)

            if length == "":
                break
            lengthInt = int(length)
            inputString = stringBreakdown[:lengthInt]
            fullStrings.append(inputString)

            newString = stringBreakdown[lengthInt:]
            stringBreakdown = newString

        return fullStrings


