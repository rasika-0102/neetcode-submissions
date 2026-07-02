class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for words in strs:
            asci = [0] * 26
            for letter in words:
                asci[ord(letter) - ord('a')] += 1

            res[tuple(asci)].append(words)
        return list(res.values())

        