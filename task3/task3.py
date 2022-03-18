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

    def square_compare(self, other_sq):#функция возвращает True, если площадь self меньше другой фигуры
        return self._s < other_sq

    def perimeter_compare(self, other_p):#функция возвращает True, если периметр self меньше другой фигуры
        return self._p < other_p

class Box(Figure):
    def __init__(self,a):
        self._a=a
        self._p=self.get_perimeter()
        self._s=self.get_square()
    def get_perimeter(self):
        p=4*self._a
        return (p)
    def get_square(self):
        s=self._a*self._a
        return (s)


class Rectangle(Figure):
    def __init__(self,a,b):
        self._a=a
        self._b=b
        self._p=self.get_perimeter()
        self._s=self.get_square()
    def get_perimeter(self):
        p=2*(self._a+self._b)
        return (p)
    def get_square(self):
        s=self._a*self._b
        return (s)

class Circle(Figure):
    def __init__(self,r):
        self._r=r
        self._p=self.get_perimeter()
        self._s=self.get_square()
    def get_perimeter(self):
        p=2*self._r*self.PI
        return (p)
    def get_square(self):
        s=self.PI*self._r*self._r
        return (s)
class Triangle(Figure):
    def __init__(self,a,b,c):
        self._a=a
        self._b=b
        self._c=c
        self._p=self.get_perimeter()
        self._pp=self._p/2
        self._s=self.get_square()
    def get_perimeter(self):
        p=self._a+self._b+self._c
        return (p)
    def get_square(self):
        s=(self._pp * (self._pp - self._a) * (self._pp - self._b) * (self._pp - self._c)) ** (1 / 2)
        return (s)
figure1=Box(5)
print(figure1.get_perimeter())
print(figure1.get_square())
figure2=Circle(3)
print(figure2.get_perimeter())
print(figure2.get_square())
print(figure2.perimeter_compare(figure1.get_perimeter()))
figure3=Triangle(3,4,5)
print(figure3.get_square())