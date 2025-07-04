from typing import List
from collections import defaultdict
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l =0
        r = len(heights) -1
        maxArea = 0

        while l < r:
            lenght = r - l
            height = min(heights[l],heights[r])
            area = lenght * height
            maxArea = max(maxArea, area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxArea
