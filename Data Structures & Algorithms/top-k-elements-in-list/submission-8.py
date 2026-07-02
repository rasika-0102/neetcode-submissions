class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        minheap = []

        for v in count:
            heapq.heappush(minheap, (count[v], v))

        while len(minheap) > k:
            heapq.heappop(minheap)

        for val in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
        


        