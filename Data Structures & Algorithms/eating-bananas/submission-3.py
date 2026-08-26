import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        speed = right
        while left <=right:
            mid = (left+right)//2
            hours_needed = 0
            for p in piles:
                hours_needed += math.ceil(p/mid)
            if hours_needed <= h:
                speed = mid
                right = mid-1
            else:
                left = mid+1
        return speed
