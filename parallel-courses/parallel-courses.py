from collections import defaultdict, deque


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        prev_courses = defaultdict(set)
        next_courses = defaultdict(set)
        
        for prev_course, next_course in relations:
            next_courses[prev_course].add(next_course)
            prev_courses[next_course].add(prev_course)
        
        queue = deque()
        
        for i in range(1, n + 1):
            if i not in prev_courses:
               queue.append(i)
            
        taken = 0
        semesters = 0
        
        while queue:
            for _ in range(len(queue)):
                c = queue.popleft()
                taken += 1
                
                for nxt in next_courses[c]:
                    prev_courses[nxt].remove(c)
                    if not prev_courses[nxt]:
                        queue.append(nxt)
            semesters += 1
        
        if taken < n:
            return -1
        
        return semesters