#LSP - Liskov Substitution Principle

# The Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
# This means that if a class is a subclass of another class, it should be able to be used in place of the superclass without any issues.



class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float) -> None:
        self._width = value

    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    @property   
    def area(self) -> float:
        return self._width * self._height
    
    def __str__(self) -> str:
        return f'Rectangle(width={self._width}, height={self._height})'

class Square(Rectangle):
    def __init__(self, size: float):
        super().__init__(size, size)
    
    @Rectangle.width.setter
    def width(self, value: float) -> None:
        self._width = value
        self._height = value
    
    @Rectangle.height.setter
    def height(self, value: float) -> None:
        self._width = value
        self._height = value

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected_area = w * 10
    assert rc.area == expected_area, f'Expected area {expected_area}, but got {rc.area}'
    print(f'Area is {rc.area} {expected_area}')

rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)