import csv

presets= [0]          # список всех пресетов 
zap = []              # список cтрок с повторяющимися пресетами


def found_preset():     # Эта функция проходит по файлу csv построчно и пополняет список(presets)
    with open('result.csv', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        for stringg in reader:
            if len(stringg[1]):
                presets.append(int(stringg[1]))


def found_repeat_presets(presets):  #фун. для поиска и подсчёта всех повторяющихся пресетов из списка
    counter = {}

    for elem in presets:
        counter[elem] = counter.get(elem, 0) + 1

    pepa=[element for element, count in counter.items() if count > 1]
    return(pepa)


'''
for i in repeat:     #функция для добавления всех записей с одним пресетом в список
    with open('result_copy.csv', newline='') as f:
        reader = csv.reader(f, delimiter='|')
        for stringg in reader:
            if str(i) == stringg[1]:
                zap.append(stringg[1])
'''

found_preset()
repeat = found_repeat_presets(presets)
print(repeat) #(34109)