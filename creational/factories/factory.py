from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

# class Point:
#     def __init__(self, x: int, y: int, coordinate_system: CoordinateSystem = CoordinateSystem.CARTESIAN):
#         if coordinate_system == CoordinateSystem.CARTESIAN:
#             self.x = x
#             self.y = y
#         elif coordinate_system == CoordinateSystem.POLAR:
#             self.x = x * cos(y)
#             self.y = x * sin(y)

#     def __str__(self):
#         return f"Point({self.x}, {self.y})"

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return f"Point(x: {self.x}, y: {self.y})"
    
#     @staticmethod
#     def new_cartesian_point(x, y):
#         return Point(x, y)
    
#     @staticmethod
#     def new_polar_point(rho, theta):
#         return Point(rho * cos(theta), rho * sin(theta))

class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point(x: {self.x}, y: {self.y})"

    class PointFactory:
        @staticmethod
        def new_cartesian_point(self, x: float, y: float) -> 'Point':
            p = Point()
            p.x = x
            p.y = y
            return p

        @staticmethod
        def new_polar_point(self, rho: float, theta: float) -> 'Point':
            return Point(rho * cos(theta), rho * sin(theta))
    
    factory = PointFactory()

if __name__ == "__main__":
    p1 = Point.factory.new_cartesian_point(1, 2)
    print(p1)  # Point(x: 1, y: 2)

    p2 = Point.factory.new_polar_point(5, pi / 4)
    print(p2)  # Point(x: 3.5355339059327378, y: 3.5355339059327373)