import json
import numpy

data = []

ein_r = 1
zwei_r = 2.5
drei_r = 7.5
vier_r = 30

for ergebnis in numpy.arange(200,210,0.5):
    print(ergebnis)
    for reihen in range(int(ergebnis)+1):
        current = []
        count = 0
        for einer in range(int(ergebnis)+1):
            for zweier in range(int(ergebnis/2.5)+2):
                for dreier in range(int(ergebnis/7.5)+2):
                    for vierer in range(int(ergebnis/30)+2):
                        if ein_r * einer + zwei_r * zweier + drei_r * dreier + vier_r * vierer == ergebnis:
                            if einer + 2*zweier + 3*dreier + 4*vierer == reihen:
                                current.append([einer,zweier,dreier,vierer])
                                count += 1

        int_of_data = len(data)
        data.append({"Ergebnis":ergebnis, "Reihen": reihen, "Moeglichkeiten": count, "Kombinationen": []})
        if len(current):
            for i in range(len(current)):
                data[int_of_data]["Kombinationen"].append(current[i])
    json.dump(data, open('/home/matthies/Documents/Coding/Python/AndererStuff/log200-210.json', 'w'), indent = 4)
