class Solution:
    def numDecodings(self, s: str) -> int:
        
        my_map = {len(s) : 1}

        for i in range (len(s) - 1, -1, -1):
            if s[i] == "0": 
                my_map[i] = 0
            else:
                my_map[i] = my_map[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or 
                s[i] == "2" and s[i + 1] in "0123456"):

                my_map[i] += my_map[i + 2]

        return my_map[0]
        

        

            




        