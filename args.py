''' Example with tuples: '''
def ArgumentsTuples(*args): #print a tuple, received  by the four line
    print(args)

answer = ArgumentsTuples("Sergio", 27, True, 0.28)
print(answer)

''' Example with dictionary '''
def ArgumentsDic(**kwargs):#Print a dictionary, and its necessary the double *
    print(kwargs)

answer = ArgumentsDic(valor = 3,nombre = "Vanessa", decimals = 5.5,bolead = False)
print(answer)

''' Example add in with a loop '''

def add_tuples(*args):
    resultado = 0
    for valor in args:
        resultado = resultado + valor
    print(resultado)

resultado = add_tuples(3, 6, 7, 7, 8)
print(resultado)