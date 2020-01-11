""" def palindromo(frase): #variable local - All functions made on a "function"
    frase = frase.replace(" ","")# local variable
    print("Print replace function =", frase)
    return frase == frase[::-1]


frase = "anita lava la tina"
resultado = palindromo(frase)#Global varible
print("Print the normal sentence =", frase)
print("Print the answer that return on palindromo function =", resultado)
 """
def palindromo():
    #we can acces to a global varible without a call
    nw_valor = frase.replace(" ","")# local variable
    print("Print replace function =", frase)
    return frase == frase[::-1]

frase = "anita lava la tina"
resultado = palindromo()#Global varible
print("Print the normal sentence =", frase)
print("Print the answer that return on palindromo function =", resultado)

