#!/usr/bin/python3

#To avoid this process of the next taskself.
''' _list = [] #false
for valor in range(0,101):
    _list.append(valor)
print(_list)
 '''

''' _list = [ 'x cosa'  for valor in range(0,101)]
print(_list)
 '''
#listas
_list = [ value  for value in range(0,101) if value % 2 == 0]
print(_list)
#1 - valor agregar a lista
#2 - Un ciclo, for
#3 - Conditon  return just pairs

#Tuple
_tupla = tuple((value  for value in range(0,101) if value % 2 == 0))
print(_tupla)
#1 - valor agregar a lista
#2 - Un ciclo, for
#3 - Conditon  return just pairs

#Dictionary 

_dictionary = { indice:valor for indice, valor in enumerate(_list) if indice < 10}
print(_dictionary)