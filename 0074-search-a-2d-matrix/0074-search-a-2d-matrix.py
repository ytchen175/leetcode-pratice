class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_row(matrix, target):
            top, bottom = 0, len(matrix) - 1

            if (top == bottom): # 只有一個 row
                return top # 其實 return bottom 也可以

            while (top <= bottom):
                mid = top + (bottom - top) // 2

                if matrix[mid][-1] < target: # mid row 的最後一個元素都比 target 小
                    top = mid + 1 # 代表 target 在下面
                elif matrix[mid][0] > target: # mid row 的第一個元素比 target 大
                    bottom = mid - 1 # 代表 target 在上面
                else:
                    # matrix[mid][-1] >= target or matrix[mid][0] <= target
                    # 代表 target 要在 matrix[mid] 這條找
                    return mid

            return -1

        row_idx = find_row(matrix, target)

        if row_idx == -1:
            return False
        
        # binary search
        arr = matrix[row_idx]
        left, right = 0, len(arr) - 1
        
        while (left <= right):
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False