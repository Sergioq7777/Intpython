#!/usr/bin/python3

my_string = "Hello World!"

my_string ='''Este es un string\n y un salto de linea ''' 

course = "love u"
name = "Mother"

final_message = "No se por q"+ course + "tanto"+ name
final_message1 = "No se por q %s tanto %s" %(course, name)
final_message2 = "No se por q {} tanto {}" .format(course, name)

print(my_string)
print(final_message)
print(final_message1)
print(final_message2)