from abc import ABC, abstractmethod
class Figure(ABC):
    def __init__(self):
        self._s = 0.0
        self._p = 0.0
    @abstractmethod
    def get_square(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass

    def square_compare(self, other_sq):#функция возвращает True, если площадь self меньше другой фигуры
        return self._s < other_sq

    def perimeter_compare(self, other_p):#функция возвращает True, если периметр self меньше другой фигуры
        return self._p < other_p

class Box(Figure):
    def __init__(self,a):
        self._p=4*a
        self._s=a*a
    def get_perimeter(self):
        return (self._p)
    def get_square(self):
        return (self._s)

class Rectangle(Figure):
    def __init__(self,a,b):
        self._p=2*(a+b)
        self._s=a*b
    def get_perimeter(self):
        return (self._p)
    def get_square(self):
        return (self._s)

class Circle(Figure):
    def __init__(self,r):
        self._p=2*3.1415*r
        self._s=3.1415*r*r
    def get_perimeter(self):
        return (self._p)
    def get_square(self):
        return (self._s)
class Triangle(Figure):
    def __init__(self,a,b,c):
        self._p=a+b+c
        pp=self._p/2
        self._s=(pp*(pp-a)*(pp-b)*(pp-c))**(1/2)
    def get_perimeter(self):
        return (self._p)
    def get_square(self):
        return (self._s)
cvadr=Box(5)
print(cvadr.get_perimeter())
print(cvadr.get_square())
ttt=Rectangle(3,4)
print(ttt.get_perimeter())
print(ttt.perimeter_compare(cvadr.get_perimeter()))
treug=Triangle(3,4,5)
print(treug.get_square())