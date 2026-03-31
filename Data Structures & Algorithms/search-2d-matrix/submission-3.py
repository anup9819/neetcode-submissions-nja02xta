class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        low, high = 0, r*c-1
        while low<=high:
            mid = (low+high)//2
            row = mid//c
            column = mid%c
            if target == matrix[row][column]:
                return True
            if target < matrix[row][column]:
                high = mid-1
            else:
                low=mid+1
        return False