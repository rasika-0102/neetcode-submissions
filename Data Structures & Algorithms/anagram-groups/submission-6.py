class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)

        for s in strs:
            sortedS = sorted(s)
            joinS = "".join(sortedS)

            my_map[joinS].append(s)
        return list(my_map.values())
        