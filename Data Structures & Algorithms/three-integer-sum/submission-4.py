class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = []

        for start in range(len(sorted_nums) - 2):
            # Avoid checking duplicate start numbers
            if start > 0 and sorted_nums[start] == sorted_nums[start - 1]:
                continue

            middle = start + 1
            end = len(sorted_nums) - 1

            while middle < end:
                total = sorted_nums[start] + sorted_nums[middle] + sorted_nums[end]

                if total == 0:
                    triplet = [sorted_nums[start], sorted_nums[middle], sorted_nums[end]]
                    if triplet not in output:
                        output.append(triplet)
                    middle += 1
                    end -= 1
                elif total < 0:
                    middle += 1  # Sum is too small; move middle right to increase it
                else:
                    end -= 1     # Sum is too large; move end left to decrease it

        return output