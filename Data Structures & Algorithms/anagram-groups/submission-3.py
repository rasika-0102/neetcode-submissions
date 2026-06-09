class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_map = defaultdict(list)
        res =[]

        for s in strs:
            sortedS = ''.join(sorted(s))
            my_map[sortedS].append(s)
        return list(my_map.values())

        