def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        
        left = 0
        right = R * C  - 1
        
        while left <= right:
            mid = (left + right) // 2
            midVal = matrix[mid//C][mid%C]
            if target == midVal: 
                return True
            if target < midVal: 
                right = mid - 1
            else: 
                left = mid + 1
        
        return False