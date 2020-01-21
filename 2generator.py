def generador(*args):
    """ Hola mundo jejeje """
    for valor in args:
        yield valor, True if valor > 5 else False


nombre = generador.__name__
documentacion = generador.__doc__
print(nombre)
print(documentacion)