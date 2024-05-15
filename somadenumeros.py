'''
Soma de números: Solicite ao usuário para digitar uma série de números e use um loop "while" para somá-los.
O loop continua até que o usuário digite um número negativo para indicar que terminou.
'''
quant = int(input())
contador = quant
resultado = 0
while contador > 0:
    obj = int(input("some os numeros: "))
    resultado = resultado + obj
    contador = contador - 1
print("o seu resultado é", resultado)
     
