class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        my_set = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in my_set or
                word[i] != board[r][c]):
                return False

            
            my_set.add((r, c))

            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1) )

            my_set.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
        

        