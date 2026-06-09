class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1

            my_map[tuple(arr)].append(s)

        return list(my_map.values())
            
        