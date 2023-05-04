class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        stack = []

        output = ""

        for char in s:
            if char.lower() in vowels:
                stack.append(char)

        for char in s:
            if char.lower() in vowels:
                output += stack.pop()
            else:
                output += char

        return output