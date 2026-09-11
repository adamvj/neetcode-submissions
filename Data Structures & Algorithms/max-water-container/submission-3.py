class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        largest = 0
        while start < end:
            length = end - start
            lower = min(heights[start], heights[end])
            if length*lower > largest:
                largest = length*lower
            if heights[start] > heights[end]:
                end-=1
            else:
                start +=1
        return largest
        