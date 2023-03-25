''' Практические задания по теме Объектно-ориентированного программирования '''
''' ЗАДАНИЕ 1 '''
class Student:
    def __init__(self, name='Ivan', age=18, group_number='10A'):
        self.name = name
        self.age = age
        self.groupNumber = group_number

    def getName(self):
        return f'Имя студента - {self.GetName}'

    def getAge(self):
        return f'Возраст студента - {self.GetAge}'

    def getGroupNumber(self):
        return f'Группа студента - {self.GetGroupNumber}.'

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, group_number):
        self.groupNumber = group_number

''' ЗАДАНИЕ 2 '''
class math:
    def __init__(self,a=0,b=0):
        self.a = a
        self.b = b

    def addition(self, a, b):
        print(a + b)

    def multiplication(self, a, b):
        print(a * b)

    def division(self, a, b):
        print(a / b)

    def subtraction(self, a, b):
        print(a - b)

''' ЗАДАНИЕ 3 '''
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def on(self):
        print("Автомобиль заведен")

    def off(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color

    def get_all(self):
        print("У автомобиля цвет ->", self.color)
        print("У автомобиля тип ->", self.type)
        print("У автомобиля год выпуска ->", self.year)