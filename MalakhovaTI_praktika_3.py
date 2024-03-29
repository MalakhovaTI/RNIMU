''' Практические задания по темам (Классы в языке Python. Определение
данных, методов, операций. Наследование. Множественное наследование.
Композиция при разработке классов.) '''

''' ЗАДАНИЕ 1. Исправьте в коде все ошибки так, чтобы скрипт заработал'''
print('ЗАДАНИЕ 1.')
class SuperClass():
    # Конструктор суперкласса.
    def __init__(self, num = 0):
        self.num = num
    # Метод суперкласса.
    def get_num(self):
        print(self.num)
    # Создаем подкласс.

class SubClass(SuperClass):
    # Конструктор подкласса.
    def __init__(self, num = 0):
        SuperClass.__init__(self, num)
    # Вызываем конструктор суперкласса.
        print('Экземпляр создан!')

# Создаем 1-й экземпляр подкласса.
obj_1 = SubClass(10)
# Выводим значение атрибута.
print(obj_1.num)
# Создаем 2-й экземпляр подкласса.
obj_2 = SubClass(5)
# Выводим значение атрибута.
obj_2.get_num()
print()

''' ЗАДАНИЕ 2. Создайте простейший в мире класс SimplePass. Затем создайте экземпляр
класса и выведите на экран его тип '''
print('ЗАДАНИЕ 2.')
class SimplePass:
    pass
simp = SimplePass()
print(type(simp))
print()

''' ЗАДАНИЕ 3. Определите класс A, включающий:
     строку документирования класса 'Класс A';
     метод set_a() для установки значения атрибута a;
     метод get_a() для получения значения этого атрибута.
Выведите на экран документацию класса. Затем создайте первый экземпляр класса и 
при помощи определенных методов установите и выведите на экран значение его атрибута a.
Далее создайте второй экземпляр класса, после чего также установите и выведите на 
экран значение атрибута a, но уже при помощи прямого доступа к атрибуту по точке.'''

print('ЗАДАНИЕ 3.')
class A:
    '''Класс A'''

    def set_a(self, a = 0):
        self.a = a

    def get_a(self):
        return self.a


print(A.__doc__)

obj_1 = A()
obj_1.set_a(1)
print(obj_1.get_a())

obj_2 = A()
obj_2.a = 2
print(obj_2.a)
print()

''' ЗАДАНИЕ 4. Определите класс B, включающий:
     строку документирования класса 'Класс B';
     конструктор, инициализирующий атрибут данных b создаваемых экземпляров;
     метод get_b() для получения значения этого атрибута.
Выведите на экран документацию класса. Затем создайте экземпляр
класса obj и при помощи метода экземпляра выведите на экран значение его
атрибута b'''

print('ЗАДАНИЕ 4.')
class B:
    '''Класс B'''

    def __init__(self, b = 0):
        self.b = b

    def get_b(self):
        return self.b


print(B.__doc__)

obj = B(15125)
print(obj.get_b())
print()

''' ЗАДАНИЕ 5. Определите класс C, наследующий классы A (задача №3) и B (задача №4) и включающий:
     строку документирования класса 'Класс C = A + B';
     конструктор, инициализирующий дополнительно атрибуты
    данных a и c создаваемых экземпляров;
     собственные методы set_b() и set_c() для установки значений
    соответствующих атрибутов;
     собственный метод get_c() для получения значения атрибута c.
Выведите на экран документацию класса. Затем создайте экземпляр класса obj,
после чего при помощи соответствующих методов экземпляра выведите на
экран значения его атрибутов a, b и c.'''

print('ЗАДАНИЕ 5.')
class C(A, B):
    '''Класс C = A + B'''
    def __init__(self, a = 0, b = 0, c = 0):
        B.__init__(self, b)
        self.a = a
        self.c = c

    def set_b(self, b):
        self.b = b

    def set_c(self, c):
        self.c = c

    def get_c(self):
        return self.c

print(C.__doc__)

obj = C(1,2,3)
print(obj.get_a())
print(obj.get_b())
print(obj.get_c())
print()

''' ЗАДАНИЕ 6. Определите класс D, включающий:
     статический метод stat_print_dict, выводящий на экран словарь атрибутов
    переданного ему объекта класса;
     метод класса cls_print_dict, выводящий на экран словарь атрибутов своего
    класса.
Создайте экземпляр класса obj и, вызвав оба метода из этого экземпляра,
выведите на экран словарь атрибутов класса D. Объясните различие в
использовании методов'''

print('ЗАДАНИЕ 6.')

class D:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def stat_print_dict(D):
        print(D.a, D.b, D.c)

    def cls_print_dict(self):
        print(self.a, self.b, self.c)
