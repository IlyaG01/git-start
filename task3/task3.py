from abc import ABC, abstractmethod
import math

class Figure(ABC):
    PI = 3.1415
    def __init__(self):
        self._s = 0.0
        self._p = 0.0

    @abstractmethod
    def get_square(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass

    def compare_square(self, other_sq):#функция возвращает True, если площадь self меньше другой фигуры
        return self._s < other_sq

    def compare_perimeter(self, other_p):#функция возвращает True, если периметр self меньше другой фигуры
        return self._p < other_p

class Box(Figure):
    def __init__(self,a):
        self._a=a
        self._p=self.get_perimeter()
        self._s=self.get_square()
    def get_perimeter(self):
        return (4*self._a)
    def get_square(self):
        return (self._a*self._a)


class Rectangle(Figure):
    def __init__(self,a,b):
        self._a=a
        self._b=b
        self._p=self.get_perimeter()
        self._s=self.get_square()
    def get_perimeter(self):
        return (2*(self._a+self._b))
    def get_square(self):
        return (self._a*self._b)

class Circle(Figure):
    def __init__(self,r):
        self._r=r
        self._p=self.get_perimeter()
        self._s=self.get_square()
    def get_perimeter(self):
        return (2*self._r*self.PI)
    def get_square(self):
        return (self.PI*self._r*self._r)
class Triangle(Figure):
    def __init__(self,a,b,c):
        self._a=a
        self._b=b
        self._c=c
        self._p=self.get_perimeter()
        self._pp=self._p/2
        self._s=self.get_square()
    def get_perimeter(self):
        return (self._a+self._b+self._c)
    def get_square(self):
        return ((self._pp * (self._pp - self._a) * (self._pp - self._b) * (self._pp - self._c)) ** (1 / 2))
figure1=Box(5)
print(figure1.get_perimeter())
print(figure1.get_square())
figure2=Circle(3)
print(figure2.get_perimeter())
print(figure2.get_square())
print(figure2.compare_perimeter(figure1.get_perimeter()))
figure3=Triangle(3,4,5)
print(figure3.get_square())