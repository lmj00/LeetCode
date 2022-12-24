class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        
        for i in range(len(names)):
            for j in range(len(heights)):
                if heights[i] > heights[j]:
                    names[i], names[j] = names[j], names[i]
                    heights[i], heights[j] = heights[j], heights[i]
                    
        return names       
