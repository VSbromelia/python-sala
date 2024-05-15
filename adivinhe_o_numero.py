# Adivinhar o número: Faça um jogo simples onde o programa escolhe um número aleatório entre 1 e 100, e o usuário tenta adivinhar.
# O loop "while" continua até que o usuário adivinhe corretamente.

adivinhe = int(input("Adivinhe o numero: "))
adivi = 1
while adivinhe != adivi:
    adivi = int(input("Tente novamente: "))
    if adivi == 1 or adivinhe == 1:
      print("Acertou")
    break
