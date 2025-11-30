import math

class shape:
    def claculate_area(self):
        pass
class circle(shape):
    def __init__(self,radi):
        self.radi=radi
    def calculate_area(self):
        return math.pi*self.radi*self.radi
class rectngle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def calculate_area(self):
        return self.b*self.l   
shapes=[circle(2),rectngle(2,2)]
for s in shapes:
    print(f"calculated area is",s.calculate_area())    
