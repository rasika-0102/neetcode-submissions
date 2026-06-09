class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crstopre = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            crstopre[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if crstopre[crs] == []:
                return True
            
            visited.add(crs)

            for pre in crstopre[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)

            crstopre[crs] = []
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

            

        