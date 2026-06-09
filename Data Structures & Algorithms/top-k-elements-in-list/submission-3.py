class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for n in nums: 
            count[n] = 1 + count.get(n, 0)                          #1. count = {1: 1, 2: 2, 3: 3}

        minheap = []

        for n in count:
            heapq.heappush(minheap, [count[n], n])                  #minheap = [1: 1, 2: 2, 3: 3]

            while len(minheap) > k:																	#minheap = [2: 2, 3: 3]
                heapq.heappop(minheap)

        res = []
        for i in range (k):																					#minheap = [2: 2, 3: 3]
            res.append(heapq.heappop(minheap)[1])

        return res

        