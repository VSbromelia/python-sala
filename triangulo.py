'''
Determinar o tipo de triângulo:
Solicite ao usuário os comprimentos dos três lados de um triângulo e crie um programa para determinar se é equilátero, isósceles ou escaleno.

'''
l1 = float(input())
l2 = float(input())
l3 = float(input())

if l1 == l2 and l1 == l3:
    print("seu triangulo é equilatero")
elif l1 != l2 and l1 != l3:
    print("seu triangulo é escaleno")
else:
    print("seu triangulo é isósceles")
