class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:      #check if index is expired
                q.popleft()

            if (r + 1) >= k:    #check if window size is reached
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output