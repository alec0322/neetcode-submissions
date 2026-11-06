class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        rowToNums = defaultdict(set)
        colToNums = defaultdict(set)
        boxToNums = defaultdict(set)

        for r in range(rows):
            for c in range(cols):
                n = board[r][c]
                box = self.getBoxForPosition(r, c)

                if n != '.':
                    if n in rowToNums[r]:
                        return False
                    else:
                        rowToNums[r].add(n)

                    if n in colToNums[c]:
                        return False
                    else:
                        colToNums[c].add(n)

                    if n in boxToNums[box]:
                        return False
                    else:
                        boxToNums[box].add(n)
        
        return True

    def getBoxForPosition(self, r: int, c: int) -> int:
        if r < 3:
            if c < 3:
                return 0
            elif 3 <= c < 6:
                return 1
            else:
                return 2
        elif 3 <= r < 6:
            if c < 3:
                return 3
            elif 3 <= c < 6:
                return 4
            else:
                return 5
        else:
            if c < 3:
                return 6
            elif 3 <= c < 6:
                return 7
            else:
                return 8

