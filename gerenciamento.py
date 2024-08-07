#gerenciamento reunioes
par = int(input())
tipo = input()
if par <= 5:
    reuniao = "Sala pequena"
elif par <= 15:
    reuniao = "Sala Média"
else:
    reuniao = "Sala grande"

print(reuniao)
