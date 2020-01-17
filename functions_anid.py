''' Creating a function who calls other to make a validation '''
def validation(num1, num2):
    return num1 > 0 and num2 > 0
def division(num1, num2):
    if validation(num1, num2):
        return num1 / num2

result = validation(5, 2)
div = division(5, 2)
print(result)
print(div)

''' Creating a function inside other function '''

def dv(n1, n2):
    def val():
        return n1 > 0 and n2 > 0
    if val():
        return n1 / n2
answer = dv(20, 2)
print(answer)


''' Creating closure - function create function '''

def create_function(n1, n2):
    def validation():
        return n1 > 0 and n2 > 0
    return n1 / n2
new_Function = create_function(20, -2)
print(new_Function)



''' Creating closure - function create function '''

def create_function(n1, n2):
    def validation():
        return n1 > 0 and n2 > 0
    return validation
def apply_function(func):
    resultado = func()
    print(resultado)

new_Function = create_function(20, -2)
apply_function(new_Function)