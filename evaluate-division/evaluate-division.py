from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        store = defaultdict(dict)

        for eq, val in zip(equations, values):
            store[eq[0]][eq[1]] = val
            store[eq[1]][eq[0]] = 1 / val

        answers = []
        visited = set()
        
        def dfs(curr_node, target_node, acc_product=1):
            visited.add(curr_node)

            for neighbour in store[curr_node]:
                if neighbour == target_node:
                    return acc_product * store[curr_node][target_node]

            for neighbour, value in store[curr_node].items():
                if neighbour in visited:
                    continue
                result = dfs(neighbour, target_node, acc_product * value)
                if result != -1.0:
                    return result
            
            return -1.0

        for dividend, divisor in queries:
            if dividend not in store or divisor not in store:
                answers.append(-1.0)
            elif dividend == divisor:
                answers.append(1.0)
            else:
                answers.append(dfs(dividend, divisor))
                visited = set()

        return answers