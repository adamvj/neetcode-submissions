class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = []

        #prefix
        prefix_prod = [1] * n
        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        #suffix
        suffix_prod = [1] * n
        for i in range(n-2, -1, -1):
            suffix_prod[i] = suffix_prod[i+1] * nums[i+1]
        for i in range(n):
            product = prefix_prod[i] * suffix_prod[i]
            results.append(product)
        return results
        