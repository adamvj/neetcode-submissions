class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        longest = 0
        
        for num in unique_nums:
            if num-1 not in unique_nums:
                current_num = num
                current_len = 1

                while current_num+1 in unique_nums:
                    current_num+=1
                    current_len+=1
                longest = max(longest, current_len)
        return longest