class Solution:

  def longestConsecutive(self, nums: list[int]) -> int:
    num_set = set(nums)  # O(n) space and time lookup
    longest = 0

    for num in num_set:
      # Only start counting if 'num' is the start of a sequence
      if num - 1 not in num_set:
        current_num = num
        streak = 1

        while current_num + 1 in num_set:
          current_num += 1
          streak += 1

        longest = max(longest, streak)

    return longest