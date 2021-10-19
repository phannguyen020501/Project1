class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print("Name: {}".format(self.name))

    def getAge(self):
        print("Age: {}".format(self.age))

    def getSex(self):
        print("Sex: {}".format(self.sex))

class Male(Person):
    sex = "Male"

male = Male("Phan Ngoc Nguyen",20)
male.getName()
male.getAge()
male.getSex()
print("-------------------------")
class Foo:
    name = "Foo"
    def getName(self):
        print("Class: Foo")

class Bar(Foo):
    name = "Bar"
    def getName(self):
        print("Atribute name= "+ super().name)
        super().getName()

Bar().getName()
print("--------------------------")
#da ke thua

class First:
    def getFirst(self):
        print("class first")

class Second:
    def getSecond(self):
        print("class second")

class Third(First, Second):
    def getThird(self):
        print("clas third")

third = Third()
third.getFirst()
third.getSecond()
third.getThird()
print("----------------------")
#truyen vao 2 ke thua thi super ke thua cai dau tien
class First1:
    def getClass(self):
        print("Class first")
class Second1:
    def getClass(self):
        print("Class second")
class Third1(First1, Second1):
    def getClass(self):
        super().getClass()
third1 = Third1()
third1.getClass()
print("--------------------")
class First2:
    def getClass(self):
        print("Class first")
        super().getClass()
class Second2:
    def getClass(self):
        print("Class second")
class Third2(First2, Second2):
    def getClass(self):
        super().getClass()
third2 = Third2()
third2.getClass()
print("----------------------")
