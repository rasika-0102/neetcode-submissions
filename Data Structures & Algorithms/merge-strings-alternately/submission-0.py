class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        merge = []

        while i < len(word1) and j < len(word2):
            merge.append(word1[i])
            merge.append(word2[j])
            i += 1
            j += 1
        merge.append(word1[i:])
        merge.append(word2[j:])
        return "".join(merge)



      