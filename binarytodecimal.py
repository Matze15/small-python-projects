toConv = input('Binary to decimal system: ')

inZS = 0
rounds = -1

for i in range(len(toConv), 0, -1):
    rounds += 1
    if(int(toConv[i-1]) == 1):
        inZS += 2**rounds

print(toConv, 'in decimal system is', inZS)