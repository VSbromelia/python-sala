'''


Calculadora de IMC (Índice de Massa Corporal):
Crie um programa que solicite ao usuário sua altura (em metros) e seu peso (em quilogramas) e calcule o IMC. Em seguida, o programa deve informar em qual faixa de IMC o usuário se encontra (abaixo do peso, peso normal, sobrepeso, etc.).
O cálculo do IMC é feito dividindo o peso (em quilogramas) pela altura (em metros) ao quadrado.

'''
altura = float(input())
massa = int(input())
imc = massa / altura**2
 
if imc < 16:
    print("magreza leve")
elif imc > 16 and imc < 17:
    print("magreza moderada")
elif imc > 17 and imc < 18.5:
    print("magreza leve")
elif imc >18 and imc  < 25:
    print("saudavel")
elif imc > 25 and imc < 30:
    print("sobrepeso")
elif imc >30 and imc < 35:
    print("obesidade")
else:
    print("obesidade morbida")
