class Solution:
    def maxArea(self, heights: List[int]) -> int:
        record_storage = 0
        start = 0
        end = len(heights)-1
        while start < end:
            lower = min(heights[start], heights[end])
            record_storage = max(lower * (end-start), record_storage)
            if heights[start] < heights[end]:
                start+=1
            else:
                end-=1
        return record_storage