class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        
        while (left < right) and (left != right):
            if arr[left] > arr[right]:
                right -= 1
                
            elif arr[left] < arr[right]:
                left += 1
            
            else:
                left += 1
                right -= 1
        
        return left