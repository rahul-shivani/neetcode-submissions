class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                elem = board[i][j]

                if elem == '.':
                    continue

                if elem in rows[i] or elem in cols[j] or elem in grids[(i//3, j//3)]:

                    return False

                rows[i].add(elem)
                cols[j].add(elem)
                grids[(i//3, j//3)].add(elem)

        return True