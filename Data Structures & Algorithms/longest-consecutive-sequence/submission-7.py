class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      uniques = set(nums)
      length = 0
      longest = 0
      for i in nums:
        if i-1 in uniques:
          continue
        else:
          while i+length in uniques:
            length+=1
            longest = max(length, longest)
          length = 0
      return max(length, longest)
        