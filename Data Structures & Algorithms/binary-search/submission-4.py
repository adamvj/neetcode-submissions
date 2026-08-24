class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)//2
            mid_val = nums[mid]
            if target == mid_val:
                return mid
            elif target > mid_val:
                start = mid+1
            else:
                end = mid-1
        return -1  

