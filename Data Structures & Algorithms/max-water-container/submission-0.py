class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        ans = 0
        while l<r:
            curr_water = (r-l)*min(heights[l],heights[r])
            ans = max(ans, curr_water)

            if heights[l]>= heights[r]:
                r -=1
            else:
                l += 1
        
        return ans