from collections import deque


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        queue = deque([s1])
        visited = {s1}
        k = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()

                if current == s2:
                    return k

                i = 0

                while current[i] == s2[i]:
                    i += 1

                for j in range(i, len(s1)):
                    if current[j] == s2[i]:
                        new_state = current[:i] + current[j] + current[i + 1:j] + current[i] + current[j + 1:]
                        if new_state not in visited:
                            queue.append(new_state)
                            visited.add(new_state)

            k += 1

        return -1