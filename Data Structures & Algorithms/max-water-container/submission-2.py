class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        max_storage = 0
        while start < end:
            distance = end - start
            lower = min(heights[start], heights[end])
            contains = distance * lower
            max_storage = max(max_storage, contains)
            if lower == heights[start]:
                start+=1
            elif lower == heights[end]:
                end-=1
        return max_storage                