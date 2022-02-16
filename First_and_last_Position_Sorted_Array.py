 def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        def binarySearch(arr, target, isFirst):
            l, r = 0, len(arr) - 1
            while l + 1 < r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    if isFirst:
                        r = mid
                    else:
                        l = mid
                elif arr[mid] < target:
                    l = mid
                else:
                    r = mid
            
            if arr[l] == target: return l
            if arr[r] == target: return r
            return -1
        
        firstIndex = binarySearch(nums, target, True)
        secondIndex = binarySearch(nums, target, False)
        return [firstIndex, secondIndex]