import csv
from optparse import Values


def found_presets():
    stroks = []
    with open('result.csv', newline='') as f:
            reader = f.readlines()
            for stringg in reader:
                if len(stringg.split('|')[1]):
                    stroks.append(stringg)
            return stroks

file = found_presets()


result = {}

for line in file:
    result.setdefault(line.split('|')[1],[]).append(line)

lopes = [elem for elem, count in result.items() if len(count) > 1]
result = {elem: count for elem, count in result.items() if len(count) > 1}

pok = []
for key, value in result.items():
    obraz = value[0]
    for i in value:
        if i!= obraz:
            pok.append(i)
        obraz = i

def write_file(pok):        # Собирает файл из списка.
    f = open( 'итоги.txt', 'w' )
    f.write("".join(pok))
    f.close
    
write_file(pok)
        
