class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for words in strs:
            arr = [0] * 26
            for letters in words:
                arr[ord(letters) - ord('a')] += 1
        
            res[tuple(arr)].append(words)
        return list(res.values())
        