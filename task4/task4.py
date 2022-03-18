from abc import ABC, abstractmethod
class Human(ABC):
    GREAT_MARK=5
    GOOD_MARK=4
    def __init__(self):
        self._fio = " "
        self._age = 0
        self._scholarship = 0
    @abstractmethod
    def get_fio(self):
        pass
    @abstractmethod
    def get_scholarship(self):
        pass

    def scholarship_compare(self, other_person):#функция возвращает True, если стипендия self меньше другого
        return self._scholarship < other_person

class Student(Human):
    GREAT_SCHOLARSHIP=6000
    GOOD_SCOLARSHIP=4000
    NO_SCOLARSHIP=0
    def __init__(self,fio,age,average_mark):
        self._fio=fio
        self._age=age
        self._average_mark=average_mark
        self._scholarship=self.get_scholarship()

    def get_scholarship(self):
        if self._average_mark==self.GREAT_MARK:
            return(self.GREAT_SCHOLARSHIP)
        if self._average_mark < self.GREAT_MARK and self._average_mark>=self.GOOD_MARK:
            return(self.GOOD_SCOLARSHIP)
        if self._average_mark<self.GOOD_MARK:
            return(self.NO_SCOLARSHIP)
    def get_fio(self):
        return (self._fio+" "+str(self._age))

class Aspirant(Human):
    GREAT_SCHOLARSHIP = 8000
    GOOD_SCOLARSHIP = 6000
    NO_SCOLARSHIP=0
    def __init__(self,fio,age,name_of_science_work,average_mark):
        self._fio=fio
        self._age=age
        self._name_of_science_work=name_of_science_work
        self._average_mark = average_mark
        self._scholarship = self.get_scholarship()

    def get_scholarship(self):
        if self._average_mark == self.GREAT_MARK:
            return (self.GREAT_SCHOLARSHIP)
        if self._average_mark < self.GREAT_MARK and self._average_mark >= self.GOOD_MARK:
            return (self.GOOD_SCOLARSHIP)
        if self._average_mark < self.GOOD_MARK:
            return (self.NO_SCOLARSHIP)

    def get_fio(self):
        return (self._fio + " " + str(self._age))

student1=Student('Ivanov Ivan Ivanovich', 20,5)
student2=Student('Smirnov Andrey Sergeevich', 22, 4.2)
student3=Student('Petrov Alex Borisovich',18,3)
master1=Aspirant('Bond James Bond', 26,'Casino Royal',5)
master2=Aspirant('Skywalker Luke Anakinovich',25,"laser sables",4.5)
master3=Aspirant('Potter Harry Jamesovich',27,'The Chamber of Secret',3.8)
print(student1.get_fio())
print(master2.get_scholarship())
print(student2.scholarship_compare(master1.get_scholarship()))
