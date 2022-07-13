
def found_presets():
    stroks = []
    with open('test.csv', newline='') as f:
            reader = f.readlines()
            for stringg in reader:
                if len(stringg.split('|')[1]):
                    stroks.append(stringg)
            return stroks

file = found_presets()


result = {}

for line in file:
    result.setdefault(line.split('|')[1],[]).append(line)

result = {elem: count for elem, count in result.items() if len(count) > 1}

trol = []
for key, value in result.items():
    for i in value:
        if i in trol:
            break
        else:
            trol.append(i)


def write_file(trol):        # Собирает файл из списка.
    f = open( 'trol.txt', 'w' )
    f.write("".join(trol))
    f.close
    
write_file(trol)