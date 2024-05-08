'''

Determinar o maior de três números:
Solicite três números ao usuário e crie um programa que determine qual deles é o maior.


'''
n1 = int(input("insira o primeiro numero: "))
n2 = int(input("insira o segundo numero: "))
n3 = int(input("insira o terceiro numero: "))

if n1 > n2 and n1 > n3:
    print(n1, "é o maior")
elif n2 > n1 and n2 > n3:
    print(n2, "é o maior")
else:
    print(n3, "é o maior")