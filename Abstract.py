class Area:
    def calculate_area(self): #Abstract
        raise NotImplementedError('Error')
    def display_area(self):
        print(self.calculate_area())


class Square(Area):
    def __init__(self,length):
        self.length = length
    def display_name(self):
        print('Square')
    #Child class must implement the parent class abstract method
    def calculate_area(self):
        return self.length**2

r = Square(3)
print(r.calculate_area())
r.display_area()