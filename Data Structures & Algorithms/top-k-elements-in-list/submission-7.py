class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n , 0)

        
        minheap = []
        for val in count:
            heapq.heappush(minheap, (count[val], val))

        while len(minheap) > k:
            heapq.heappop(minheap)
        
        for v in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
        