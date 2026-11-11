class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}

        count = Counter(nums)

        minheap = []
        for i in count:
            heapq.heappush(minheap, (count[i], i))
        
        while k < len(minheap):
            heapq.heappop(minheap)
        
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
        