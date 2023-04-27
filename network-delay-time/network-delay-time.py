from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        result = [-1] * (n + 1)

        for source, target, time in times:
            adj_list[source].append((time, target))

        min_heap = [(0, k)]

        while min_heap:
            curr_time, node = heapq.heappop(min_heap)

            if result[node] != -1:
                continue
            result[node] = curr_time

            for time, target in adj_list.get(node, []):
                heapq.heappush(min_heap, (time + curr_time, target))

        max_time = 0

        for time in result[1:]:
            if time == -1:
                return -1
            max_time = max(max_time, time)

        return max_time