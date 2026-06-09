class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    #   prefix = strs[0] 
    #  prefix_len = len(prefix)

    #   for s in strs[1:]:
    #     while prefix != s[0:prefix_len]:
    #          prefix_len -= 1

    #          if prefix_len == 0:
    #             return ""
             
    #          prefix = prefix[0:prefix_len]

    #   return prefix


        for i in range (len(strs[0])):  
            for s in strs[1:]:           
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]




        
        