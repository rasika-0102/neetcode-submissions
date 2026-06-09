class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxleft = height[l]
        maxright = height[r]
        water = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                maxleft = max(maxleft, height[l])
                water += maxleft - height[l]

            else:
                r -= 1
                maxright = max(maxright, height[r])
                water += maxright - height[r]
        return water

        