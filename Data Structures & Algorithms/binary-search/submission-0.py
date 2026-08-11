class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) -1
        while begin <= end:
            midpoint = begin + (end-begin) // 2
            mid_value = nums[midpoint]
            if mid_value == target:
                return midpoint
            elif mid_value > target:
                end = midpoint -1
            else:
                begin = midpoint+1
        return -1

