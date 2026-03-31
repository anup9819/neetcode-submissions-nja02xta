class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        column =collections.defaultdict(set)
        box = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val=='.':
                    continue
                if val in row[r] or val in column[c] or val in box[r//3,c//3]:
                    return False
                row[r].add(val)
                column[c].add(val)
                box[(r//3,c//3)].add(val)
        return True
        