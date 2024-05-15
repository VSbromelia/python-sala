'''
Soma dos números pares: Eles podem escrever um programa que solicita um número ao usuário e, em
seguida, usa um loop "while" para somar todos os números pares até esse número.
'''
quant = int(input())
contador = quant
resultado = 0
while contador > 0:
    obj = int(input("some os numeros: "))
    resultado = resultado + obj
    contador = contador - 1
print("o seu resultado é", resultado)
     