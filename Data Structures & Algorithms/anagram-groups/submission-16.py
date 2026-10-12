class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for words in strs:
            arr = [0] * 26
            for letter in words:
                arr[ord(letter) - ord('a')] += 1
            
            res[tuple(arr)].append(words)
        return list(res.values())
        