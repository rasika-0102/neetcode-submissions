class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)

            heapq.heappush(minheap, [dist, x, y])

        points = []
        while k > 0:
            dist, x, y = heapq.heappop(minheap)
            k -= 1
            points.append([x,y])
            
        return points
            

        