#/usr/bin/python3

#the normal usage loop while
"""
while condition:
    code
else:
    code
"""
cont = 0
bandera = True
""" 
while cont <= 10:
    print(cont)
    cont += 1 # increase the count in one
    if cont == 5:
        continue #continue
    if cont == 8:
        break # End before get to ten
else:
    print("loop end")

"""

while bandera:
    print(cont)
    cont += 1 # increase the count in one
    if cont == 5:
        continue #continue
    if cont == 8:
        bandera = False
else:
    print("loop end")
