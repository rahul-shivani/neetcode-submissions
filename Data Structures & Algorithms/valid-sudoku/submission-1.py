class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        gridCounts = defaultdict(set)
        rowCounts = defaultdict(set)
        colCounts = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowCounts.get(i, []):
                    return False
                if board[i][j] in colCounts.get(j, []):
                    return False
                if board[i][j] in gridCounts.get((i//3,j//3), []):
                    return False

                rowCounts[i].add(board[i][j])
                colCounts[j].add(board[i][j])
                gridCounts[(i//3,j//3)].add(board[i][j])

        return True
                
        