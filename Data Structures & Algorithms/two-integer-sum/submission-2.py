class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        approved = []
        for i in range(0, len(nums)-1, 1):
            for j in range (i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    approved.append(i)
                    approved.append(j)
        return approved

                    