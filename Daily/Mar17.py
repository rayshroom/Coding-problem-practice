'''
Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:

input and output values are in floating-point.
radius and x-y position of the center of the circle is passed into the class constructor.
a point on the circumference of the circle is considered to be in the circle.
randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
'''

from random import uniform
from math import sqrt, pi, cos, sin

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.rad = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        angle = uniform(0, 2 * pi)
        dist = sqrt(uniform(0, 1)) * self.rad
        x = self.x + dist * cos(angle)
        y = self.y + dist * sin(angle)
        
        return [x, y]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()