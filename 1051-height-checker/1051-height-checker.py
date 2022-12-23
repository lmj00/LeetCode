class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h2 = heights[:]
        heights.sort()
        count = 0
        
        for i in range(len(heights)):
            if h2[i] != heights[i]:
                count += 1
                
        return count
        
        
    