# Author: IBN (AMDG) 4/12/2022

from cmath import pi
import math
class Circle:
    """ Circle class represents a circle """

    def __init__(self):
            """ Create a new circle with radius 3 """
            self.radius = 1
    
    def get_diameter(self):
           """ Calculate diameter of circle """
           return self.radius * 2

    def get_area(self):
            """ Calculate area of circle """
            return (self.radius ** 2) * pi
    
    def get_perimeter(self):
        """ Calculate perimeter of circle """
        return self.get_diameter() * pi

my_circle = Circle()
my_circle.radius = 3
print(my_circle.get_perimeter())
