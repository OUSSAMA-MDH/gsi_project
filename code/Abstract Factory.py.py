

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def erase(self):
        pass


class Circle2D(Shape):
    def draw(self):
        print("Circle.draw2D")
    
    def erase(self):
        print("Circle.erase2D")

class Square2D(Shape):
    def draw(self):
        print("Square.draw2D")
    
    def erase(self):
        print("Square.erase2D")

class Triangle2D(Shape):
    def draw(self):
        print("Triangle.draw2D")
    
    def erase(self):
        print("Triangle.erase2D")

class Rectangle2D(Shape):
    def draw(self):
        print("Rectangle.draw2D")
    
    def erase(self):
        print("Rectangle.erase2D")


class Circle3D(Shape):
    def draw(self):
        print("Circle.draw3D")
    
    def erase(self):
        print("Circle.erase3D")

class Square3D(Shape):
    def draw(self):
        print("Square.draw3D")
    
    def erase(self):
        print("Square.erase3D")

class Triangle3D(Shape):
    def draw(self):
        print("Triangle.draw3D")
    
    def erase(self):
        print("Triangle.erase3D")

class Rectangle3D(Shape):
    def draw(self):
        print("Rectangle.draw3D")
    
    def erase(self):
        print("Rectangle.erase3D")

# Abstract Factory 
class ShapeFactory(ABC):
    @staticmethod
    @abstractmethod
    def createShape(shape_type):
        pass

# Concrete Factories 
class ShapeFactory2D(ShapeFactory):
    @staticmethod
    def createShape(shape_type):
        shape_type = shape_type.lower()
        if shape_type == "circle":
            return Circle2D()
        elif shape_type == "square":
            return Square2D()
        elif shape_type == "triangle":
            return Triangle2D()
        elif shape_type == "rectangle":
            return Rectangle2D()
        else:
            print(f"Bad shape creation: {shape_type}")
            return None

class ShapeFactory3D(ShapeFactory):
    @staticmethod
    def createShape(shape_type):
        shape_type = shape_type.lower()
        if shape_type == "circle":
            return Circle3D()
        elif shape_type == "square":
            return Square3D()
        elif shape_type == "triangle":
            return Triangle3D()
        elif shape_type == "rectangle":
            return Rectangle3D()
        else:
            print(f"Bad shape creation: {shape_type}")
            return None












if __name__ == "__main__":

    print("=" * 50)
    
    # 2D
    print("\n 2D:")
   
    
    factory_2d = ShapeFactory2D()
    shapes_2d = ["Circle", "Square", "Triangle", "Rectangle", "Unknown"]
    
    for shape_type in shapes_2d:
        shape = factory_2d.createShape(shape_type)
        if shape:
            print(f"\ncreate  {shape_type}")
            shape.draw()
            shape.erase()
    
    # 3D
    print("\n" + "=" * 30)
    print("create 3D shapes:")
    
    
    factory_3d = ShapeFactory3D()
    shapes_3d = ["Circle", "Square", "Triangle", "Rectangle"]
    
    for shape_type in shapes_3d:
        shape = factory_3d.createShape(shape_type)
        if shape:
            print(f"\ncreate {shape_type}")
            shape.draw()
            shape.erase()
    
    
    print("\n" + "=" * 30)

    
    def create_and_display(factory, shape_name, dimension):
        shape = factory.createShape(shape_name)
        if shape:
            print(f"the shape {shape_name} ({dimension}D)")
            shape.draw()
            shape.erase()
            print("-" * 20)
    
    #factories
    create_and_display(ShapeFactory2D, "circle", "2")
    create_and_display(ShapeFactory3D, "circle", "3")
    create_and_display(ShapeFactory2D, "square", "2")
    create_and_display(ShapeFactory3D, "square", "3")
    
    print("\n" + "=" * 50)
