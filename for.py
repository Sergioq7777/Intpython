#!/usr/bin/python3

_list = [1,2,3,4,5,6,7,8,9,10]

for valor in _list:
    pass

#The range can be used with just one number too.
# for(i=0; i <= 27; 4+)
#In range from 0 to 27, in pairs.
new_range = range(0,27,2)
for valor in new_range:
    pass

#print listas
'''
indice = 0
for valor in _list:
    print(valor, "indice", indice)
    indice += 1
 '''
for indice, valor in  enumerate(_list):
 pass # print(valor, "indice", indice)

for valor in range(0, len(_list)):
    pass #print(valor)

indice = 0
for valor in "Curso de codigo facilito":
    pass #print(valor)

dictionary = {"Nombre" : "Sergio", "Last Name" : "Quiroga", "CC" : 102033, "Cell" : "31865665"}
for Clave, Valor in dictionary.items():
    print("Complete the {} : {}".format(Clave, Valor))

