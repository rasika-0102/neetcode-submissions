class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stn for stn in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:

            firstStone = - heapq.heappop(maxheap)
            secondStone = - heapq.heappop(maxheap)

            if secondStone < firstStone:
                heapq.heappush(maxheap, -(firstStone - secondStone))
            
        return -maxheap[0] if maxheap else 0
        