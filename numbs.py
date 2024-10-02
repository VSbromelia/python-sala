#soma de numeros de 1 a 100
n = 0
x = 0
s = 1
while True:
    print(f"soma {x} = {n - 1} + {s}")
    x += 1
    s = x - n 
    n = n + 1
    if n > 100:
        break
