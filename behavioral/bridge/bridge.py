# circle square
# vector raster

#VectorCircle vectorSquare rasterSquare rasterCircle
from abc import ABC, abstractmethod

class Renderer(ABC):
    def render_circle(self, radius: float) -> None:
        pass
    #render_square
    def render_square(self, side: float) -> None:
        pass

class VectorRenderer(Renderer):
    def render_circle(self, radius: float) -> None:
        print(f"Drawing a vector circle with radius {radius}")

    def render_square(self, side: float) -> None:
        print(f"Drawing a vector square with side {side}")

class RasterRenderer(Renderer):
    def render_circle(self, radius: float) -> None:
        print(f"Drawing a raster circle with radius {radius}")

    def render_square(self, side: float) -> None:
        print(f"Drawing a raster square with side {side}")
    
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def draw(self) -> None:
        pass

    def resize(self, factor: float) -> None:
        pass

class Circle(Shape):
    def __init__(self, radius: float, renderer: Renderer):
        super().__init__(renderer)
        self.radius = radius

    def draw(self) -> None:
        self.renderer.render_circle(self.radius)

    def resize(self, factor: float) -> None:
        self.radius *= factor
    
if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(5, raster)
    circle.draw()  # Drawing a raster circle with radius 5
    circle.resize(2)
    circle.draw()  # Drawing a raster circle with radius 10
    circle = Circle(5, vector)
    circle.draw()  # Drawing a vector circle with radius 5
    circle.resize(2)
    circle.draw()  # Drawing a vector circle with radius 10