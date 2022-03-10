from abc import ABC, abstractmethod
class Human(ABC):
    def __init__(self):
        self._fio = " "
        self._age = 0
        self._salary = 0
    @abstractmethod
    def get_fio(self):
        pass
    @abstractmethod
    def get_salary(self):
        pass

    def salary_compare(self, other_person):#функция возвращает True, если стипендия self меньше другого
        return self._salary < other_person

class Student(Human):
    def __init__(self,fio,age,average_mark):
        self._fio=fio
        self._age=age
        if average_mark==5:
            self._salary=6000
        if average_mark < 5 and average_mark>=4:
            self._salary = 4000
        if average_mark<4:
            self._salary=0
    def get_fio(self):
        return (self._fio+" "+str(self._age))
    def get_salary(self):
        return (self._salary)

class Aspirant(Human):
    def __init__(self,fio,age,name_of_science_work,average_mark):
        self._fio=fio
        self._age=age
        self._name_of_science_work=name_of_science_work
        if average_mark==5:
            self._salary=8000
        if average_mark < 5 and average_mark>=4:
            self._salary = 6000
        if average_mark<4:
            self._salary=0
    def get_fio(self):
        return (self._fio+" "+str(self._age))
    def get_salary(self):
        return (self._salary)

student1=Student('Ivanov Ivan Ivanovich', 20,5)
student2=Student('Smirnov Andrey Sergeevich', 22, 4.2)
student3=Student('Petrov Alex Borisovich',18,3)
master1=Aspirant('Bond James Bond', 26,'Casino Royal',5)
master2=Aspirant('Skywalker Luke Anakinovich',25,"laser sables",4.5)
master3=Aspirant('Potter Harry Jamesovich',27,'The Chamber of Secret',3.8)
print(student1.get_fio())
print(master2.get_salary())
print(student2.salary_compare(master1.get_salary()))
