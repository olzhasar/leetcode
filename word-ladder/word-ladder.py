from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        paths = defaultdict(list)

        wordList.append(beginWord)

        for i, source in enumerate(wordList):
            for j, word in enumerate(wordList[i:]):
                diff_count = 0
                for char1, char2 in zip(source, word):
                    if char1 != char2:
                        diff_count += 1
                        if diff_count > 1:
                            break
                if diff_count == 1:
                    paths[source].append(word)
                    if source != beginWord:
                        paths[word].append(source)

        queue = deque([(beginWord, 1)])
        visited = set()

        while queue:
            word, acc_count = queue.popleft()
            if word in visited:
                continue
            visited.add(word)
            if word == endWord:
                return acc_count
            
            for path in paths[word]:
                if path not in visited:
                    queue.append((path, acc_count + 1))

        return 0