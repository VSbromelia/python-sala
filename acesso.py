#acesso
funcio = input()
dia = input()

if funcio == "gerente" and "analista":
    if dia == "segunda" or dia == "terça" or dia == "quarta" or dia == "quinta" or dia == "sexta" or dia == "sábado" or dia == "domingo":
        print("acesso liberado")
elif funcio == "estagiário":
    if dia == "segunda" or dia == "terça" or dia == "quarta" or dia == "quinta" or dia == "sexta": 
        print("acesso autorizado")
    elif dia == "domingo" or dia == "sábado":
        print("acesso negado")
