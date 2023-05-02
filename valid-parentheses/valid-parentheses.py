class Solution:
    def isValid(self, s: str) -> bool:
        open_mapping = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []

        for char in s:
            if char in open_mapping:
                stack.append(char)
            else:
                try:
                    prev = stack.pop()
                except IndexError:
                    return False
                if char != open_mapping[prev]:
                    return False

        return not stack