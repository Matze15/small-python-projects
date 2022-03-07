import math

bis = float(input('Show prime numbers up to: '))

for i in range(2,round(bis)+1):
    prim = True
    for k in range(2,round(math.sqrt(i))+1):
        if i%k == 0:
            prim = False
            break
    if prim:
        print(i)