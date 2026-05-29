class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ## Search for potential row
        t = 0
        b = len(matrix)-1
        potentialRow = -1
        while t<=b:
            mid = (t+b)//2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                potentialRow = mid
                break
            elif matrix[mid][0] >= target:
                b = mid-1
            else:
                t = mid+1

        if potentialRow == -1:
            return False

        l = 0
        r = len(matrix[potentialRow])-1
        while l<=r:
            mid = (l+r)//2
            if matrix[potentialRow][mid] == target:
                return True
            elif matrix[potentialRow][mid]>target:
                r = mid-1
            else:
                l = mid+1
        
        return False


