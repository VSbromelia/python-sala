#pedidos
valor = int(input())
dias = int(input())
if valor < 100 and dias > 7:
    classi = "Normal"
elif valor >= 100 and dias >= 4 and dias <= 7:
    classi = "Prioritário"
elif valor > 500 and dias < 4:
    classi = "Urgente"

print(classi)
