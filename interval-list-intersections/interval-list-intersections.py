class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        
        output = []  # intersection
        
        i = j = 0
        
        # two pointers
        # iterate two lists at once
        # if the el from the first list is to the left from second, shift the first pointer
        # if the list is to the left from second, move first pointer
        
        while i < len(firstList) and j < len(secondList):
            first, second = firstList[i], secondList[j]
            
            if first[0] > second[1]:
                j += 1
            elif second[0] > first[1]:
                i += 1
            else:
                output.append([max(first[0], second[0]), min(first[1], second[1])])
                if second[1] >= first[1]:
                    i += 1
                elif first[1] >= second[1]:
                    j += 1
                    
        return output