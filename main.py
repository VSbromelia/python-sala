'''
Verificar se um número é positivo, negativo ou zero:
Peça ao usuário para inserir um número e, em seguida, escreva um programa para determinar se o número é positivo, negativo ou zero.

'''
n = int(input("insira um numero: "))

if n > 0:
    print("seu numero é positivo")
elif n < 0:
    print("seu numero é negativo")
else:
    print("seu numero é zero")