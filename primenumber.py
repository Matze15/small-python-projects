import math

#get user input
zahl = int(input('Is this a prime number? - Number: '))

prim = True

for i in range(2,round(math.sqrt(zahl))+1):
    if zahl%i == 0:
        prim = False
        break

if zahl == 1:
    print('1 is not a prime number.')
elif prim:
    print(zahl, 'is a prime number.')
else:
    print(zahl, 'is not a prime number.')