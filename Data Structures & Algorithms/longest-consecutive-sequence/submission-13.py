class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        longest = 1
        current = 1

        for i in range(1, len(nums)):
            # Skip duplicate numbers
            if nums[i] == nums[i - 1]:
                continue
            # Next consecutive element found
            elif nums[i] == nums[i - 1] + 1:
                current += 1
            # Sequence broken, reset streak
            else:
                longest = max(longest, current)
                current = 1

        return max(longest, current)