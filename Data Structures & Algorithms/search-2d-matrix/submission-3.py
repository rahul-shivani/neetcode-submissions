class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l<=r:
            m = (l+1)//2 + r//2
            row, col = m//len(matrix[0]), m%len(matrix[0])
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                l = m+1
            else:
                r = m-1
        
        return False

