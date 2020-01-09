#!/usr/bin/python3
diccionario = { 'a' : 55, 5 : "string", (1,2) : False }

diccionario['c'] = 'new string' #create clave/valor
diccionario['a'] =  "You're the best" #change the  value

print(diccionario)
#obtain data from diccionario
valor = diccionario['a']
print(valor)

#If it doesn't find the clave , return ...
valor = diccionario.get('z', "Error")
print(valor)

#Delete values
#del diccionario[2]

#Print all keys and values  in a list mode
_keys = list(diccionario.keys())
print(_keys)

_values = list(diccionario.values())
print(_values)

#Print all keys and values  in a tuples mode
_keys = tuple(diccionario.keys())
print(_keys)

_values = tuple(diccionario.values())
print(_values)

#Diccionario dos
diccionario_dos = {'b' : 2, 'c' : 3, 'd' : 4}

#extender diccionario

diccionario.update(diccionario_dos)
print(diccionario)


