class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        area=self.length*self.width
        print("Area of a rectangle :",area)
    
    def perimeter(self):
        perimeter=2*(self.length+self.width)
        print("Perimeter of a rectangle :",perimeter)

class box(rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height

    def volume(self):
        volume=self.length*self.width*self.height
        print("Volume of a box :",volume)
    
    def perimeter(self):
        super().perimeter()
        p=4*(self.length+self.width+self.height)
        print("Perimeter of a box :",p)
    
length=int(input("Enter the length :"))
width=int(input("Enter the width :"))
height=int(input("Enter the height :"))
b=box(length,width,height)
b.area()
b.perimeter()
b.volume()