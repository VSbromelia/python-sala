'''
exercicio de for
1- imprimir de um a dez
2- imprimir elementos de uma lista
3- imprimir caracteres de uma string
4- contar numeros de uma lista maior que zero
'''
#1
for n in range(1, 11):
  print(n)
#2
lista = ["Microsoft Windows", "macOS", "Linux", "OS/2", "DOS"]
for l in lista:
    print(l, end=" ")
  
#3
palavra = "Minecraft"
for p in palavra:
    print(p)
numeros = [10, -1, 5, 4, -9, -12]

#4
contador = 0
for numero in numeros:
    if numero > 0:
        contador += 1

print("na lista são", contador, "numeros maiores que zero")
