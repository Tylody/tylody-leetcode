# Return true if the Sudoku board is valid, otherwise return false

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numDict = {}
        for i in board:
            numDict = {}
            for j in i:
                if j == ".":
                    continue

                if j in numDict:
                    print("FLAG 1")
                    return False

                numDict[j] = True

        for i in range(9):
            numDict = {}
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in numDict:
                    print("FLAG 2")
                    print(numDict)
                    print(str(board[j][i]))
                    print(str(i) + " " + str(j))
                    return False

                numDict[board[j][i]] = True

        for i in range(3):
            for j in range(3):
                numDict = {}
                for k in range(3):
                    for l in range(3):
                        currentSquare = board[i * 3 + k][j * 3 + l]
                        if currentSquare == ".":
                            continue
                        if currentSquare in numDict:
                            print("FLAG 3")
                            return False
                        numDict[currentSquare] = True

        return True

