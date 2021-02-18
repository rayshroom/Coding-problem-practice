'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

class Solution:
    def maxArea(self, height) -> int:
        leftWall = 0
        rightWall = len(height) - 1
        currArea = 0

        while leftWall < rightWall:
            lowestWall = min(height[leftWall], height[rightWall])
            wallDist = rightWall - leftWall
            currArea = max(currArea, lowestWall * wallDist)
            if height[leftWall] < height[rightWall]:
                leftWall += 1
            else:
                rightWall -= 1
        
        return currArea

soln = Solution()

h1 = [1,8,6,2,5,4,8,3,7] # 49
h2 = [1,1] # 1
h3 = [4,3,2,1,4] # 16
h4 = [1,2,1] # 2

print(soln.maxArea(h1))
print(soln.maxArea(h2)) 
print(soln.maxArea(h3)) 
print(soln.maxArea(h4)) 

assert soln.maxArea(h1) == 49
assert soln.maxArea(h2) == 1
assert soln.maxArea(h3) == 16
assert soln.maxArea(h4) == 2