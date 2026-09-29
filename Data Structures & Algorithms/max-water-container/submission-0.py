class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        maxarea=float('-inf')
        right=len(heights)-1
        while left<=right:
            area=(right-left)*(min(heights[left],heights[right]))
            maxarea=max(area,maxarea)
            if heights[left]<heights[right]:
                left=left+1
            else:
                right=right-1

        return maxarea            


        