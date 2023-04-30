import heapq
from collections import deque, defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj_list = defaultdict(list)
        # source: (target, bus_num)

        for i, route in enumerate(routes):
            for j in range(1, len(route)):
                adj_list[route[j-1]].append((route[j], i))
            if route[-1] != route[0]:
                adj_list[route[-1]].append((route[0], i))

        # num of buses, current stop, current bus
        heap = [(0, source, None)]
        visited = defaultdict(lambda: float("inf"))

        while heap:
            num_buses, curr_stop, curr_bus = heapq.heappop(heap)

            if visited[curr_stop] < num_buses:
                continue
            visited[curr_stop] = num_buses

            for adj, adj_bus in adj_list[curr_stop]:
                heapq.heappush(heap, (num_buses + int(adj_bus != curr_bus), adj, adj_bus))

        if visited[target] == float("inf"):
            return -1
        return visited[target]