class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(minheap, [dist, x, y])
        
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(minheap)
            k -= 1
            res.append([x,y])
        return res



        