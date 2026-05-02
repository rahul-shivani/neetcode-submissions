class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows =  [set() for i in range(0,9)]
        cols =  [set() for i in range(0,9)]
        grids = [[set() for i in range(0,3)] for j in range(0,3)]

        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != '.' and \
                    (board[i][j] in rows[i] \
                    or board[i][j] in cols[j] \
                    or board[i][j] in grids[i//3][j//3]):
                    # print(i, j, board[i][j] in rows[i], board[i][j] in cols[j], board[i][j] in grids[i//3][j//3])
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grids[i//3][j//3].add(board[i][j])
            
        return True

