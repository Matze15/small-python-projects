import math
import random
import os

ein_r = 1
zwei_r = 2.5
drei_r = 7.5
vier_r = 30

total = 0   

for einer in range(51):
    for zweier in range(26):
        for dreier in range(17):
            for vierer in range(7):
                if ein_r * einer + zwei_r * zweier + drei_r * dreier + vier_r * vierer == 205:
                    if einer + 2*zweier + 3*dreier + 4*vierer == 50:
                        print('Neue Möglichkeit: Einer:', einer, 'Zweier:', zweier, 'Dreier:', dreier, 'Vierer:', vierer)
                        total += 1


print('Möglichkeiten insgesamt:',total)