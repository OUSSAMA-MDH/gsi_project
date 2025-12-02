import sys

class Shape:
    def draw(self):
        pass  

    def erase(self):
        pass


class Circle(Shape):
    def draw(self): print("Circle.draw from circle class")
    def erase(self): print("Circle.erase  from circle class")
class Square(Shape):
    def draw(self): print("Square.draw from square class")
    def erase(self): print("Square.erase from square class")


class Triangle(Shape):
    def draw(self): print("triangle.draw  from triangle class")
    def erase(self): print("triangle.erase from triangle class")
class Rectangle(Shape):
    def draw(self): print("rectangle.draw from rectangle class")
    def erase(self): print("rectangle.erase from rectangle class")



class ShapeFactory:
    @staticmethod
    def createShape(type):
        if type == "Circle": return Circle()
        elif type == "Square": return Square()
        if type == "triangle": return Triangle()
        elif type == "rectangle": return Rectangle()
        else:
            print ("Bad shape creation: " + type)
            #sys.exit(1)



class ShapeFactory_scr(ShapeFactory):
    @staticmethod
    def createShape(type):
        if type == "Circle": return Circle()
        elif type == "Square": return Square()
        elif type == "rectangle": return Rectangle()
        else:
            print ("Bad shape creation: " + type)
            #sys.exit(1)


class ShapeFactory_sct(ShapeFactory):
    @staticmethod
    def createShape(type):
        if type == "Circle": return Circle()
        elif type == "Square": return Square()
        if type == "triangle": return Triangle()
        else:
            print ("Bad shape creation: " + type)
            #sys.exit(1)


            
if __name__ == "__main__":
    for type in ("Circle", "Square" ,"Circle", "Square"):
        shape = ShapeFactory.createShape(type)
        shape.draw()
        shape.erase()
    print("testing scr factory\n","="*30)
    for type in ("Circle", "Square","rectangle" ,"Circle", "Square"):
        shape = ShapeFactory_scr.createShape(type)
        shape.draw()
        shape.erase()
    print("testing sct factory\n","="*30)
    for type in ("Circle", "Square","triangle" ,"Circle", "Square", "triangle"):
        shape = ShapeFactory_sct.createShape(type)
        shape.draw()
        shape.erase()