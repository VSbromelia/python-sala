'''
Verificar se um ano é bissexto:
Peça ao usuário para inserir um ano e escreva um programa para determinar se o ano é bissexto ou não.

'''
ano = int(input())

if (ano % 4 == 0) and (ano % 100 != 0):
    print("seu ano é bissexto")
else:
    print("seu ano nao é bissexto")