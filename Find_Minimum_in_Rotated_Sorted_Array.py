class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        l, r = 0, n - 1
        
        if nums[r] > nums[l]: return nums[l]
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]: return nums[mid+1]
            if nums[mid] < nums[mid-1]: return nums[mid]
            if nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1