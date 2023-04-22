class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        prefix = ""
        postfix = ""
        
        for s in strs:
            prefix += f"{len(s)},"
            postfix += s

        return prefix[:-1] + "@" + postfix
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        delim_index = s.find("@")

        prefix = s[:delim_index]
        postfix = s[delim_index + 1:]
        output = []

        for el in prefix.split(','):
            l = int(el)
            output.append(postfix[:l])
            postfix = postfix[l:]

        return output

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))