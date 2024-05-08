'''

Classificação de Idade:
Escreva um programa que leia a idade de uma pessoa e determine se ela é criança (menor de 12 anos), adolescente (entre 13 e 19 anos), adulta (entre 20 e 59 anos) ou idosa (60 anos ou mais).

'''
i = int(input())

if i < 12:
    print("voce é menror de idade")
elif i >= 13 and i <=19:
    print("voce é adolescente")
elif i >= 20 and i <= 59:
    print("voce é adulto")
elif i >= 60: 
    print("voce é idoso")