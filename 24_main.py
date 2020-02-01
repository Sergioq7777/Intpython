''' import calculadora

resultado = calculadora.suma(35, 35)
print(resultado)

resultado = calculadora.resta(35, 35)
print(resultado)

resultado = calculadora.mul(35, 35)
print(resultado)

resultado = calculadora.div(35, 35)
print(resultado)
 '''
from calculadora import div as divide
from calculadora import suma, resta, mul

resultado = suma(35, 35)
print(resultado)

resultado = resta(35, 35)
print(resultado)

resultado = mul(35, 35)
print(resultado)

resultado = divide(35, 35)
print(resultado)