print(''' Задание № 1 ''', '\n')
import re

name = 'folder1/folder2/file.ext'
print('Расширение файла ->', re.search('\.(.+$)', name)[1], '\n')

print(''' Задание № 2 ''', '\n')
from http import client

connection = client.HTTPConnection('www.google.com')
connection.request('GET', '/')
res = connection.getresponse()
print(res.read(), '\n')

print(''' Задание № 3 ''', '\n')
import calendar

print('Расположение файла модуля calendar:', calendar.__file__)
print('Список доступных атрибутов модуля calendar:', dir(calendar))
print('Является ли 2027 год високосным? ->', calendar.isleap(2027))
print('25 июня 1995 года был', calendar.weekday(1995, 6, 25), 'день в неделе', '\n')
print(calendar.calendar(2023))