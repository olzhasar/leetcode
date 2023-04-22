class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        mapping = {}
        letters = set()
        
        for i, word in enumerate(words):
            if word in mapping:
                if mapping[word] != pattern[i]:
                    return False
            else:
                if pattern[i] in letters:
                    return False
                mapping[word] = pattern[i]
            letters.add(pattern[i])
                
        return True