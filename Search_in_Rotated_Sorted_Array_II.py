class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r)// 2
            if nums[m] == target: return True
            elif nums[m] > nums[l]:
                if nums[m] > target and nums[l] <= target:
                    r = m
                else:
                    l = m + 1
            elif nums[m] < nums[l]:
                if nums[m] < target and nums[r] >= target:
                    l = m + 1
                else:
                    r = m
            else:
                l += 1
        
        return False