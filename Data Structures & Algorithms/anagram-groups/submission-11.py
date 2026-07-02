class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for words in strs:
            op = [0] * 26
            for s in words:
                op[ord(s) - ord('a')] += 1
            
            res[tuple(op)].append(words)
        return list(res.values())
    

        