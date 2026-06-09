class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []

        for s in stones:
            heapq.heappush(maxheap, -s)
        
        while len(maxheap) > 1:
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)

            if x < y:
                weight = y - x
                heapq.heappush(maxheap, -weight)

        return -maxheap[0] if len(maxheap) > 0  else 0
                
        

            


        