#!/usr/bin/python3

fruit = 'kiwi'
fruit2 = 'apple'

#The long(.c) way
if fruit == 'pera':
    print("El valor es {}".format(fruit))
elif fruit2 == 'pera':
    print("No es {}, es {} ...".format(fruit, fruit2))
elif fruit2 == 'pera':
    pass # To avoid the indent error
else:
    print("No son ninguna")

#The fast(.py) way
fast1 =  "El valor es {}".format(fruit) if fruit == "kiwi" else "No es {}, es {}...".format(fruit, fruit2)
print(fast1)

# < > >= <= != ==
#True = 1
#False = 0
# Falsos si estan vacios [] {} () 0 '' Falso None
# Any_valor = != 0 = True

value = None
value_two = 23

#with "and" - the two must to be true.
if value and value_two > 21:
    print("es vdd")
else:
    print("no es vd")

#with "or" - one must to be true.
if value or value_two > 21:
    print("es vdd")
else:
    print("no es vd")


