import bisect
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        l = len(tickets)
        
        flights = defaultdict(list)
        
        for dep, dest in tickets:
            bisect.insort(flights[dep], dest)
            
        current = []

        def dfs(dep, k=0):
            current.append(dep)
            
            if k == l:
                return current
            
            dests = sorted(flights[dep])
            for i, dest in enumerate(dests):
                del flights[dep][i]
                res = dfs(dest, k + 1)
                if res:
                    return res
                flights[dep].insert(i, dest)
                    
            current.pop()
        
        return dfs("JFK")