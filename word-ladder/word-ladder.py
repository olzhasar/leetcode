from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        paths = defaultdict(list)

        wordList.append(beginWord)
        n = len(wordList)

        for i in range(n):
            for j in range(i + 1, n):
                diff_count = 0
                for char1, char2 in zip(wordList[i], wordList[j]):
                    if char1 != char2:
                        diff_count += 1
                        if diff_count > 1:
                            break
                if diff_count == 1:
                    paths[i].append(j)
                    if i != n - 1:
                        paths[j].append(i)

        queue = deque([(n - 1, 1)])
        visited = set()

        while queue:
            idx, acc_count = queue.popleft()
            visited.add(idx)
            if wordList[idx] == endWord:
                return acc_count
            
            for path in paths[idx]:
                if path not in visited:
                    queue.append((path, acc_count + 1))

        return 0