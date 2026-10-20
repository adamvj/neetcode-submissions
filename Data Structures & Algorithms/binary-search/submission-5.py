class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums)-1
        while begin <= end:
            midpoint = begin+(end-begin)//2
            print("current midpoint: ", midpoint)
            midpoint_val = nums[midpoint]
            print("Current midpoint val: ", midpoint_val)
            if midpoint_val == target:
                return midpoint
            elif midpoint_val < target:
                begin = midpoint+1
            else:
                end = midpoint -1
        return -1