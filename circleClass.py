import math
class Circle:
    def __init__(self,R):
        self.r=R
    def area(self):
      return (math.pi)*self.r*self.r
    def paramiter(self):
       return 2*(math.pi)*self.r

c=Circle(float(input("Enter a redius of circle:")))
print("Area of circle:",round(c.area(),2))
print("Parameter of circle:",round(c.paramiter(),2))

# print(f"Area: {c.area():.2f}")
# print(f"Perimeter: {c.paramiter:.2f}")