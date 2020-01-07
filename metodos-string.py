#!/usr/bin/python3
course = "Curse"
my_string = "Easy code"

""" formato """
result = '{a} de {b}'.format(b = course,a = my_string)
# result = result.lower()
# result = result.upper()
# result = result-title()
print(result)

""" Busqueda """

pos = result.find('code')
count = result.count("E")
new_string = result.replace('c', 'x')
new_string2 = result.split(' ')
print(new_string2)