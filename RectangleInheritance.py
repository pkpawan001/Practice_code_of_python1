class rectangle:
    def __init__(self):
        self.l=2
        self.b=3
    def area(self):
        print(f"Area of Rectangle:{self.l*self.b}")
class cubic(rectangle):
    def __init__(self):
        super().__init__()
        self.h=4
    def volume(self):
       print(f"Volume of cube is:{self.l*self.b*self.h}")


c=cubic()
c.volume()