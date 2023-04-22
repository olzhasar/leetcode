class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        words = s.split(' ')
        for i in range(len(words)):
            if words[-i - 1]:
                result += " " + words[-i -1]

        return result[1:]