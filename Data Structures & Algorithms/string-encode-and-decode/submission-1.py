class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        return output

    def decode(self, s: str) -> List[str]:
        #print(s)
        result = []
        i = 0
        while i < len(s):
            word = ""
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1

            i += 1
            length = int(length)
            temp = i + length
            while i < temp:
                word += s[i]
                i += 1
            result.append(word)
        return result
