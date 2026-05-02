class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colCounts = [0] * 9
        rowCounts = [0] * 9
        gridCounts = defaultdict(int)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                val = int(board[i][j])
                if ((1<<val) & rowCounts[i]) or \
                    ((1<<val) & colCounts[j]) or \
                    ((1<<val) & gridCounts[(i//3,j//3)]):
                    return False

                rowCounts[i] |= (1<<val)               
                colCounts[j] |= (1<<val)
                gridCounts[(i//3,j//3)] |= (1<<val)

        return True
                
        