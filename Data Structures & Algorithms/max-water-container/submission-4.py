class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_vol = 0
        while left < right:
            if (min(heights[left], heights[right])*(right-left)) > max_vol:
                max_vol = min(heights[left], heights[right])*(right-left)
                print("New max vol: ", max_vol)
            if heights[left] > heights[right]:
                right -=1
            else:
                left+=1
        return max_vol