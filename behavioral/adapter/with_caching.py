#Adapter : A contruct which adapts the existing interface X to conform to the required interface Y.

class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
    
def draw_point(p):
    print(".", end='')

#you are given this:
class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x + width, y + height), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x, y)))

class LineToPointAdapter():
    cache = {}

    def __init__(self, line: Line):
        self.h = hash(line)
        if self.h in self.cache:
            return 

        super().__init__()

        print(f": Generating Points for line"
              f"[{line.start.x}, {line.start.y}] -> "
              f"[{line.end.x}, {line.end.y}]")
        
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(int(top), int(bottom)):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(int(left), int(right)):
                points.append(Point(x, top))
        
        self.cache[self.h] = points
    
    def __iter__(self):
        return iter(self.cache[self.h])
    
def draw_rectangle(rectangles):
    print("Drawing rectangle:")
    for rc in rectangles:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == "__main__":
    rs = [
        Rectangle(0, 0, 8, 10),
        Rectangle(10, 10, 20, 20),
        Rectangle(20, 20, 30, 30)
    ]
    draw_rectangle(rs)
    draw_rectangle(rs)
    draw_rectangle(rs)