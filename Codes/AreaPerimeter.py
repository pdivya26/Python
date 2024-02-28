class Polygon:
    def __init__(self):
        self.s1 = 0
        self.s2 = 0
        self.s3 = 0
        self.h = 0
        self.a = 0
        self.p = 0

    def area(self):
        print("Shape not Defined!")

    def perimeter(self):
        print("Shape not Defined!")
        
class Square(Polygon):
    def __init__(self):
        self.s1 = int(input("Enter side of square here : "))
        if(self.s1 > 0):
            self.area()
            self.perimeter()
        else:
            print("Invalid Dimensions!")

    def area(self):
        self.a = self.s1*self.s1
        print("Area of Square =",self.a,"units")

    def perimeter(self):
        self.p = 4*self.s1
        print("Perimeter of Square =",self.p,"units")
        
class Rectangle(Polygon):
    def __init__(self):
        self.s1 = int(input("Enter length of rectangle here : "))
        self.s2 = int(input("Enter breadth of rectangle here : "))
        if(self.s1 > 0 and self.s2 > 0):
            self.area()
            self.perimeter()
        else:
            print("Invalid Dimensions!")
            
    def area(self):
            self.a = self.s1*self.s2
            print("Area of Rectangle =",self.a,"units")

    def perimeter(self):
            self.p = 2*(self.s1 + self.s2)
            print("Perimeter of Rectangle =",self.p,"units")

class Triangle(Polygon):
    def __init__(self):
        self.s1 = int(input("Enter first side of the triangle here : "))
        self.s2 = int(input("Enter second side of the triangle here : "))
        self.s3 = int(input("Enter third side (base) of the triangle here : "))
        self.h = float(input("Enter height of triangle here : "))
        if(self.s1 > 0 and self.s2 > 0 and self.s3 > 0):
            self.area()
            self.perimeter()
        else:
            print("Invalid Dimensions!")

    def area(self):
            self.a = 0.5*(self.s3*self.h)
            print("Area of Triangle =",self.a,"units")
    def perimeter(self):
            self.p = self.s1 + self.s2 + self.s3
            print("Perimeter of Triangle =",self.p,"units")

p1 = Polygon()
while(1):
    op = int(input("\nSelect Polygon:\n1. Square\n2. Rectangle\n3. Triangle\n4. Exit\nEnter your choice here : "))
    if(op == 4):
        break
    elif(op == 1):
        Square()
    elif(op == 2):
        Rectangle()
    elif(op == 3):
        Triangle()
    else:
        print("Invalid Choice!")
