from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        result = [float("inf") for _ in range(n + 1)]

        for source, target, time in times:
            adj_list[source].append((time, target))

        min_heap = [(0, k)]

        while min_heap:
            curr_time, node = heapq.heappop(min_heap)

            if curr_time > result[node]:
                continue
            result[node] = curr_time

            for time, target in adj_list[node]:
                t = time + curr_time 
                if t < result[target]:
                    heapq.heappush(min_heap, (time + curr_time, target))

        max_time = max(result[1:])
        if max_time == float("inf"):
            return -1
        return max_time