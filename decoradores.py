''' def decorador(function):
    def new_decorator(*args, **kwargs):
        print("We are going to execute that function")
        resultado = function(*args, **kwargs)
        print(resultado)
        print("We've already execute the function")
    return new_decorator

@decorador
def greet():
    print("Hello World")

@decorador
def sum(*args):
    valor = 0
    for i in args:
        valor = valor + i
    return valor

greet()
sum(1, 7, 8)
 '''
''' Create a function that create another function and execute the decorators '''

def calculator(function):
    def create_function(*args, **kwargs):
        print("Getting the calculation")
        answer = function(*args, **kwargs)
        print("The answer is = ", answer)
        print("We've already receive the function")
    return create_function

@calculator
def add(*args):
    value = 0
    for iterator in args:
        value += iterator
    return value
''' 
@calculator
def rest(*args):
    return args - args
 '''

@calculator
def div(*args):
    value = 0
    for iterator in args:
        value = value / iterator
    return value


@calculator
def mul(*args):
    value = 0
    for iterator in args:
        value = value * iterator
    return value


add(3, 3, 3)
rest(5, 3)
div(10, 2)
mul(5, 5, 5)