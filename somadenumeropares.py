#Soma dos números pares: Eles podem escrever um programa que solicita um número ao usuário e, em seguida, usa um loop "while" para somar todos os números pares até esse número.

num = int(input("insira um numero par: "))
contador = 0
soma = 0
while contador < num:
    contador = contador + 1
    if contador % 2 == 0:
        soma = soma + contador
print("Seu resultado da soma dos numeros pares em", num, "é: ", soma)
